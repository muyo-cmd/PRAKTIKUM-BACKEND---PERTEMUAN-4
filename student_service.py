class StudentService:
    def __init__(self, repo):
        self.repo = repo

    def fetch_all_students(self, major=None):
        students = self.repo.get_all(major)
        return {"status": "success", "total": len(students), "data": students}, 200

    def get_student_by_id(self, student_id):
        student = self.repo.get_by_id(student_id)
        if not student:
            return {"status": "fail", "message": "Mahasiswa tidak ditemukan"}, 404
        return {"status": "success", "data": student}, 200

    def add_student(self, data):
        if not data:
            return {"status": "fail", "message": "Body request JSON tidak boleh kosong"}, 400

        required_fields = ['nim', 'name', 'major', 'gpa']
        for field in required_fields:
            if field not in data or data[field] is None:
                return {"status": "fail", "message": f"Atribut '{field}' wajib diisi"}, 400

        if self.repo.get_by_nim(str(data['nim'])):
            return {"status": "fail", "message": "NIM sudah terdaftar"}, 400

        try:
            gpa = float(data['gpa'])
            if gpa < 0.00 or gpa > 4.00:
                return {"status": "fail", "message": "IPK harus berada dalam rentang 0.00 - 4.00"}, 400
        except ValueError:
            return {"status": "fail", "message": "IPK harus berupa angka"}, 400

        created_student = self.repo.create(
            nim=data['nim'],
            name=data['name'],
            major=data['major'],
            gpa=gpa
        )
        return {"status": "success", "message": "Mahasiswa berhasil ditambahkan", "data": created_student}, 201

    def update_student(self, student_id, data):
        if not data:
            return {"status": "fail", "message": "Body request JSON tidak boleh kosong"}, 400

        existing_student = self.repo.get_by_id(student_id)
        if not existing_student:
            return {"status": "fail", "message": "Mahasiswa tidak ditemukan"}, 404

        if 'gpa' in data:
            try:
                gpa = float(data['gpa'])
                if gpa < 0.00 or gpa > 4.00:
                    return {"status": "fail", "message": "IPK harus berada dalam rentang 0.00 - 4.00"}, 400
            except ValueError:
                return {"status": "fail", "message": "IPK harus berupa angka"}, 400

        updated_student = self.repo.update(student_id, data)
        return {"status": "success", "message": "Data berhasil diperbarui", "data": updated_student}, 200

    def delete_student(self, student_id):
        success = self.repo.delete(student_id)
        if not success:
            return {"status": "fail", "message": "Mahasiswa tidak ditemukan"}, 404
        return {"status": "success", "message": "Data mahasiswa berhasil dihapus"}, 200