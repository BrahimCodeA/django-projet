from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
User = get_user_model()

def signup(request):
    if request.method == "POST":
        # Récupérer les données du formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Vérifier la non-existence des champs
        if not (username and password and confirm_password):
            messages.error(request, "Remplissez tous les champs.")
            return render(request, 'accounts/signup.html')

        # Vérifier la longueur du mot de passe
        if len(password) < 8:
            messages.error(request, "Le mot de passe doit contenir au moins 8 caractères.")
            return render(request, 'accounts/signup.html')

        # Vérifier la longueur du nom d'utilisateur
        if len(username) < 4:
            messages.error(request, "Le nom d'utilisateur doit contenir au moins 4 caractères.")
            return render(request, 'accounts/signup.html')

        # Vérifier si un utilisateur avec le même nom d'utilisateur existe déjà
        existing_user = User.objects.filter(username=username).first()
        if existing_user:
            messages.error(request, "Un compte avec ce nom d'utilisateur existe déjà. Utilisez un nom d'utilisateur différent.")
            return render(request, 'accounts/signup.html')

        # Vérifier si les mots de passe correspondent
        if password == confirm_password:
            # Créer un utilisateur uniquement si les mots de passe correspondent
            user = User.objects.create_user(username=username, password=password)

            # Connecter automatiquement l'utilisateur
            login(request, user)

            # Rediriger vers la page d'accueil
            return redirect('home')
        else:
            # Ajouter un message d'erreur si les mots de passe ne correspondent pas
            messages.error(request, "Les mots de passe ne correspondent pas.")

    # Si la méthode de la requête n'est pas POST ou si les mots de passe ne correspondent pas,
    # afficher le formulaire d'inscription
    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
          # Vérifier la non-existence des champs
        if not (username and password):
            messages.error(request, "Remplissez tous les champs.")
            return render(request, 'accounts/login.html')

        # Vérifier si le mot de passe est fourni
        if not password:
            messages.error(request, "Le mot de passe est obligatoire.")
            return render(request, 'accounts/login.html')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            utilisateur = form.cleaned_data['utilisateur']
            email = form.cleaned_data['email']
            message_content = form.cleaned_data['message']

            EmailMessage(
                'Contact Form Submission from {}'.format(utilisateur),
                message_content,
                'dekushopcontact@gmail.com',
                ['daoudi.ibrahimd@gmail.com'],
                reply_to=[email]
            ).send()

            messages.success(request, "Votre message a bien été envoyé !")
            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'accounts/contact.html', {'form': form})




           


