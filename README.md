# REST API Mahasiswa - Refactored Layered Architecture

Proyek ini merupakan hasil refactoring dari tugas Pertemuan 3 dengan menerapkan arsitektur berlapis (*Separation of Concerns*), Flask Blueprint, dan Application Factory.

## 📐 Arsitektur & Alur Kerja Sistem

```text
  +-----------------+
  |     Client      |
  | (cURL/Postman)  |
  +--------+--------+
           |
           | 1. HTTP Request (GET/POST/PUT/DELETE)
           v
  +-------------------------------------------------------+
  | Blueprint Route (app/routes/student_routes.py)        |
  | - Menerima parameter, JSON body, dan metode HTTP      |
  +--------+----------------------------------------------+
           |
           | 2. Panggil fungsi Service
           v
  +-------------------------------------------------------+
  | Service (app/services/student_service.py)             |
  | - Aturan Bisnis 1: NIM wajib unik                    |
  | - Aturan Bisnis 2: IPK bernilai 0.00 s/d 4.00        |
  +--------+----------------------------------------------+
           |
           | 3. Akses/Simpan data jika validasi lolos
           v
  +-------------------------------------------------------+
  | Repository (app/repositories/student_repo.py)         |
  | - Memanipulasi dataset mahasiswa in-memory            |
  +--------+----------------------------------------------+
           |
           | 4. Return Data Object
           v
  +-------------------------------------------------------+
  | Service -> Route -> Client                             |
  | - Membentuk JSON Response terstandar & HTTP Status    |
  +-------------------------------------------------------+
