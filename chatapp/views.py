from django.shortcuts import render
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from .models import Message

load_dotenv()

# Initialize the Groq API model
model = ChatGroq(model="llama-3.1-8b-instant")

def chat_view(request):
    if request.method == "POST":
        user_text = request.POST.get("message")
        if user_text:
            # Call Groq API
            result = model.invoke(user_text)
            
            # Save both user and bot messages
            Message.objects.create(user_text=user_text, bot_text=result.content)

    # Fetch last 20 messages
    chat_history = Message.objects.order_by("timestamp")[:20]
    return render(request, "chatapp/chat.html", {"chat_history": chat_history})
