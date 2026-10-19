from flask import Blueprint, jsonify, request
from app.repositories.student_repo import StudentRepository
from app.services.student_service import StudentService

student_bp = Blueprint('students', __name__, url_prefix='/api/v1/students')

# Dependency Injection Layer Repository dan Service
student_repo = StudentRepository()
student_service = StudentService(student_repo)

@student_bp.route('', methods=['GET'])
def get_students():
    major_query = request.args.get('major')
    resp, code = student_service.fetch_all_students(major=major_query)
    return jsonify(resp), code

@student_bp.route('/<int:student_id>', methods=['GET'])
def get_student(student_id):
    resp, code = student_service.get_student_by_id(student_id)
    return jsonify(resp), code

@student_bp.route('', methods=['POST'])
def create_student():
    data = request.get_json() if request.is_json else None
    resp, code = student_service.add_student(data)
    return jsonify(resp), code

@student_bp.route('/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json() if request.is_json else None
    resp, code = student_service.update_student(student_id, data)
    return jsonify(resp), code

@student_bp.route('/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    resp, code = student_service.delete_student(student_id)
    return jsonify(resp), code