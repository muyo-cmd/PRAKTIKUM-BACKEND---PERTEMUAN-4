class StudentRepository:
    def __init__(self):
        # Mock Dataset Mahasiswa
        self.students = [
            {"id": 1, "nim": "202611001", "name": "Ahmad Fauzi", "major": "Teknik Informatika", "gpa": 3.75},
            {"id": 2, "nim": "202611002", "name": "Budi Santoso", "major": "Sistem Informasi", "gpa": 3.40},
            {"id": 3, "nim": "202611003", "name": "Citra Lestari", "major": "Teknik Informatika", "gpa": 3.90}
        ]

    def get_all(self, major=None):
        if major:
            return [s for s in self.students if s['major'].lower() == major.lower()]
        return self.students

    def get_by_id(self, student_id):
        return next((s for s in self.students if s['id'] == student_id), None)

    def get_by_nim(self, nim):
        return next((s for s in self.students if s['nim'] == nim), None)

    def create(self, nim, name, major, gpa):
        new_id = max([s['id'] for s in self.students], default=0) + 1
        new_student = {
            "id": new_id,
            "nim": str(nim),
            "name": name,
            "major": major,
            "gpa": float(gpa)
        }
        self.students.append(new_student)
        return new_student

    def update(self, student_id, data):
        student = self.get_by_id(student_id)
        if not student:
            return None
        
        student['name'] = data.get('name', student['name'])
        student['major'] = data.get('major', student['major'])
        student['gpa'] = float(data.get('gpa', student['gpa']))
        return student

    def delete(self, student_id):
        student = self.get_by_id(student_id)
        if not student:
            return False
        self.students = [s for s in self.students if s['id'] != student_id]
        return True