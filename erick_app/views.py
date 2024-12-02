from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Payment, Student

# Create your views here.
def home(request):
    return render(request, 'index.html')

def error(request):
    return render(request, 'error.html')

def payment(request):
    total = request.GET.get('total', None)  # Retrieve 'total' from the query string
    if total is None:
        return HttpResponse("Total amount not provided", status=400)
    return HttpResponse(f"Payment amount is {total}")

def history(request):
    return render(request, 'history.html')

def menu(request):
    return render(request, 'menu.html')

def menu_payment(request, total):
    context = {'total': total}
    return render(request, 'menu/payment.html', context)

def payment_with_total(request, total):
    # Assume total is the amount to be paid
    user = request.user  # Current logged-in user (replace with session or another method if needed)

    if user.is_authenticated:
        student = user.student  # Assuming the user has a related student object
        context = {'total': total, 'student': student}
        return render(request, 'menu/payment.html', context)
    else:
        raise Http404("User not authenticated")

def payment_history(request, student_id):
    # Retrieve the studentId from the query parameters
    if not student_id:
        return HttpResponse("Student ID is required", status=400)

    try:
        student = Student.objects.get(id=student_id)  # Replace with your actual model lookup
        history = Payment.objects.filter(student=student)  # Fetch payments related to the student
    except Student.DoesNotExist:
        raise Http404("Student not found")

    context = {'student': student, 'history': history}
    return render(request, 'menu/payment_history.html', context)
def payment_history_for_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)  # Look up the student by ID
        history = Payment.objects.filter(student=student)  # Fetch payments related to the student
    except Student.DoesNotExist:
        raise Http404("Student not found")

    context = {'student': student, 'history': history}
    return render(request, 'menu/payment_history.html', context)



