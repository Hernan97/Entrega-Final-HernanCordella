from django.shortcuts import render

from django.http import HttpResponse

from .models import Curso, Estudiante
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import login as auth_login
from .forms import RegisterForm, LoginForm, ProfileForm

from .models import Post, Comment, Profile, ChatMessage, User
from .forms import CommentForm, PostForm

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseForbidden
from django.contrib.auth.models import User

# Create your views here.
def inicio(request):
    return render(request, "appcoder/inicio.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")

def precios(request):
    return render(request, "appcoder/precios.html")

def estudiantes(request):
    return HttpResponse("Bienvenido a la página de estudiantes")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def blog(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        introduction = request.POST.get('introduction')
        title = request.POST.get('title')  # Podrías permitir a los usuarios agregar un título también
        if content:
            Post.objects.create(title=title, introduction=introduction, content=content, user=request.user)
            return redirect('blog')
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "appcoder/blog.html", {'posts': posts})

@login_required
def newpost(request):
    if request.method == 'POST':
        title = request.POST['title']
        introduction = request.POST['introduction']
        content = request.POST['content']
        user = request.user  # Usuario logueado

        # Obtener la imagen del formulario si fue cargada
        image = request.FILES.get('image')

        # Crear una nueva instancia del modelo Post con los datos del formulario
        post = Post(title=title, introduction=introduction, content=content, user=user, image=image)
        post.save()  # Guardar el post en la base de datos

        # Redirigir a alguna página después de guardar el post, por ejemplo, a la lista de posts
        return redirect('blog')  # Asegúrate de que `some_view_name` exista

    return render(request, "appcoder/newpost.html")

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Verifica si el usuario que intenta editar el post es el creador
    if post.user != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este post.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog')  # Redirigir al perfil después de editar
    else:
        form = PostForm(instance=post)

    return render(request, 'appcoder/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Verifica si el usuario que intenta eliminar el post es el creador
    if post.user != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este post.")

    if request.method == 'POST':
        post.delete()
        return redirect('blog')  # Redirigir al perfil después de eliminar

    return render(request, 'appcoder/delete_post.html', {'post': post})


def workingpage(request):
    return render(request, "appcoder/workingpage.html")

def workingpage2(request):
    return render(request, "appcoder/workingpage2.html")

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user  # Asignar el usuario autenticado
            comment.save()
            return redirect('post_detail',  post_id=post_id)
    else:
        form = CommentForm()
    comments = post.comments.all()
    return render(request, 'appcoder/post_detail.html', {
        'post': post,
        'form': form,
        'comments': comments
    })

@login_required
def profile_view(request):
    user = request.user
    posts = Post.objects.filter(user=user)
    # Intenta obtener el perfil del usuario
    profile, created = Profile.objects.get_or_create(user=user)
    # Verifica si el perfil se ha encontrado
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
        return render(request, 'appcoder/profile.html', {
        'form': form,
        'posts': posts,
        'user': user
    })


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("blog")  # Redirige a la página principal después de iniciar sesión
    else:
        form = LoginForm()
    return render(request, "appcoder/login_register.html", {'login_form': form, 'register_form': RegisterForm()})

def entregables(request):
        cursos = Curso.objects.all() # Muestra todos los cursos si no se proporciona un nombre
        nombre_curso = request.GET.get('nombre', '').strip()  # Obtiene el parámetro de búsqueda
        cursos =[]
        if nombre_curso:
            cursos = Curso.objects.filter(nombre__icontains=nombre_curso)  # Filtra los cursos por nombre
        else:
            cursos = Curso.objects.all()  # Muestra todos los cursos si no se proporciona un nombre
            no_courses_found = nombre_curso and not cursos
        estudiantes = Estudiante.objects.all()
        nombre_estudiante = request.GET.get('nombre', '').strip()  # Obtiene el parámetro de búsqueda
        estudiantes =[]
        if nombre_estudiante:
            estudiantes = Estudiante.objects.filter(nombre__icontains=nombre_estudiante)  # Filtra los estudiantes por nombre
        else:
            estudiantes = Estudiante.objects.all()  # Muestra todos los estudiantes si no se proporciona un nombre
            no_students_found = nombre_estudiante and not estudiantes
        contexto = {"cursos": cursos }
        contexto.update ({"estudiantes": estudiantes })
        contexto.update ({"no_courses_found": no_courses_found})
        contexto.update ({"no_students_found": no_students_found})
        return render(request, "appcoder/entregables.html", contexto)

def crearcurso(request):
    texto = None
    if 'nombre_curso' in request.GET and 'comision_curso' in request.GET:
        nombre_curso = request.GET.get('nombre_curso')
        comision_curso = request.GET.get('comision_curso')
        
        if nombre_curso and comision_curso:
            try:
                comision_curso = int(comision_curso)  # Convertir a entero
                curso = Curso(nombre=nombre_curso, comision=comision_curso)
                curso.save()
                texto = "Curso registrado con éxito"
            except ValueError:
                texto = "El número de comisión debe ser un número entero."
        else:
            texto = "Por favor, complete todos los campos."
    return render(request, "appcoder/crearcurso.html", {"texto": texto})

def crearestudiante(request):
    mensaje = None
    if "nombre_estudiante" in request.GET and "apellido_estudiante" in request.GET:
        nombre_estudiante = request.GET.get('nombre_estudiante')
        apellido_estudiante = request.GET.get('apellido_estudiante')
        email_estudiante = request.GET.get('email_estudiante')
        if nombre_estudiante and apellido_estudiante and email_estudiante:
            # Valida el formato del email si es necesario
            estudiante = Estudiante(nombre=nombre_estudiante, apellido=apellido_estudiante, email=email_estudiante)
            try:
                estudiante.save()
                mensaje = "Estudiante registrado con éxito"
            except Exception as e:
                mensaje = f"Error al registrar el estudiante: {e}"
        else:
            mensaje = "Por favor, complete todos los campos."
    return render(request, "appcoder/crearestudiante.html", {"mensaje": mensaje}) 

def register_view(request):
    data = {
        'form': RegisterForm()
    }
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardar el usuario en la base de datos
            form.save()
            auth_login(request, user)  # Opcional: Iniciar sesión automáticamente después del registro
            return redirect('login')  # Redirige a la página principal después del registro
        else:
            # Imprimir errores en la consola para depuración
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, "appcoder/user_register.html", data)


class CursoDetailView(DetailView):
    model= Curso
    template_name= "appcoder/entregables.html"

class CursoListView(ListView): #mostrar una lista, listar objetos
    model = Curso  #sobre que objeto vamos a trabajar
    context_object_name="cursos" #nombre con el cual le va a llegar al template
    template_name= "appcoder/entregables.html"   #template donde va a plasmar los datos

class CursoCreateView(CreateView): #crear objetos de una lista
    model = Curso  #sobre que objeto vamos a trabajar
    template_name= "appcoder/entregables.html"   #template donde va a plasmar los datos
    success_url = reverse_lazy ("entregables")
    fields = ["nombre","comision"]


@login_required
def chat(request):
    if request.method == 'POST':
        # Manejo de la creación de nuevos chats
        receiver_id = request.POST.get('receiver_id')
        try:
            receiver = User.objects.get(id=receiver_id)
            return redirect('chat_with_user', receiver_id=receiver.id)  # Redirige a la vista de chat con el usuario
        except User.DoesNotExist:
            return HttpResponse('Usuario no encontrado', status=404)
    
    # Obtén todos los mensajes de chat del usuario actual
    user = request.user
    received_chats = ChatMessage.objects.filter(receiver=user)
    sent_chats = ChatMessage.objects.filter(sender=user)
    
    # Agrega los usuarios con los que ha chateado
    chat_users = set()
    for chat in received_chats:
        chat_users.add(chat.sender)
    for chat in sent_chats:
        chat_users.add(chat.receiver)
    
    # Agrega la lista de usuarios con los que se ha chateado
    users_with_chats = list(chat_users)

    return render(request, 'appcoder/chat.html', {
        'users_with_chats': users_with_chats,
    })

@login_required
def chat_with_user(request, receiver_id):
    try:
        receiver = User.objects.get(id=receiver_id)
    except User.DoesNotExist:
        return HttpResponse('Usuario no encontrado', status=404)
    
    # Obtén los mensajes de chat entre el usuario actual y el receptor
    user = request.user
    chat_messages = ChatMessage.objects.filter(sender=user, receiver=receiver) | ChatMessage.objects.filter(sender=receiver, receiver=user)
    chat_messages = chat_messages.order_by('timestamp')
    
    if request.method == 'POST':
        # Maneja el envío de un nuevo mensaje
        message = request.POST.get('message')
        if message:
            ChatMessage.objects.create(sender=user, receiver=receiver, message=message)
    
    return render(request, 'appcoder/chat_with_user.html', {
        'receiver': receiver,
        'chat_messages': chat_messages,
    })