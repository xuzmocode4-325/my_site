from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import date
# Create your views here.

articles = [
    {
        "slug": "ai-transforming-creative-coding",
        "image": "ai_coding.jpg",
        "author": "Xuzmonomi", 
        "date": date(2023, 3, 15),
        "title": "How AI is Transforming Creative Coding",
        "excerpt": "AI is revolutionizing the world of creative coding by enabling artists and developers to create intricate and dynamic art effortlessly.",
        "content": "Artificial Intelligence (AI) is making waves in the realm of creative coding, offering unprecedented tools and capabilities for artists and developers. By leveraging machine learning algorithms, creators can now generate complex visual patterns, interactive installations, and digital art pieces that were previously unimaginable. AI-powered generative art tools enable the creation of unique artworks by analyzing vast datasets, learning patterns, and producing intricate designs that blend creativity with computational precision. This fusion of AI and creative coding is opening up new possibilities for digital artists, pushing the boundaries of what can be achieved with code and imagination."
    },
    {
        "slug": "interactive-digital-art-ai",
        "image": "interactive_art.jpg",
        "author": "Xuzmonomi", 
        "date": date(2022, 8, 10),
        "title": "The Role of AI in Interactive Digital Art",
        "excerpt": "Interactive digital art is being reshaped by AI, allowing for more engaging and responsive installations that adapt to viewer interaction.",
        "content": "The integration of AI in interactive digital art is creating new dimensions of engagement and interactivity. AI algorithms can analyze real-time data from viewers, such as movement, gestures, and even emotions, to adapt and respond accordingly. This results in art installations that are not just reactive but also proactive, offering personalized experiences to each viewer. For instance, AI can be used to modify visual elements, soundscapes, or even the storyline of an interactive piece based on audience interaction, making each encounter unique. This dynamic interplay between AI and interactive art is transforming how we perceive and engage with digital artworks."
    },
    {
        "slug": "neural-networks-creative-coding",
        "image": "neural_networks.jpg",
        "author": "Xuzmonomi", 
        "date": date(2024, 2, 5),
        "title": "Neural Networks in Creative Coding",
        "excerpt": "Neural networks are a powerful tool in creative coding, enabling the creation of sophisticated algorithms that can generate stunning visual art.",
        "content": "Neural networks, a subset of machine learning, have found a significant place in the world of creative coding. These algorithms mimic the human brain's functioning to recognize patterns and generate outputs based on learned data. In the context of digital art, neural networks can be trained on vast collections of images, styles, and patterns to produce new and original works of art. Artists can use neural networks to create abstract visuals, transform photographs into artwork in the style of famous painters, or even generate entirely new artistic styles. The ability of neural networks to learn and evolve makes them an invaluable tool for pushing the boundaries of creativity in the digital realm."
    },
    {
        "slug": "ai-driven-visual-art",
        "image": "ai_visual_art.jpg",
        "author": "Xuzmonomi", 
        "date": date(2023, 9, 14),
        "title": "AI-Driven Innovations in Visual Art",
        "excerpt": "The advent of AI is revolutionizing visual art, providing artists with new tools to explore and expand their creative horizons.",
        "content": "AI-driven innovations are transforming visual art by providing artists with novel tools and techniques to explore their creativity. AI algorithms can analyze and replicate artistic styles, generate new compositions, and even create entirely new forms of visual expression. For instance, Generative Adversarial Networks (GANs) can be used to produce realistic images or unique abstract art that challenges traditional boundaries. AI-powered software can assist artists in refining their techniques, experimenting with new ideas, and automating repetitive tasks, thereby allowing them to focus more on the creative process. This synergy between AI and visual art is paving the way for a new era of artistic exploration and innovation."
    },
    {
        "slug": "creative-coding-and-machine-learning",
        "image": "creative_coding.jpg",
        "author": "Xuzmonomi", 
        "date": date(2022, 11, 23),
        "title": "The Intersection of Creative Coding and Machine Learning",
        "excerpt": "Machine learning is enhancing creative coding, enabling the development of sophisticated and dynamic digital art.",
        "content": "The intersection of creative coding and machine learning is fostering a new wave of innovation in digital art. Machine learning algorithms can analyze vast amounts of data, learn from it, and generate creative outputs that are both intricate and original. In creative coding, this means artists can develop algorithms that produce dynamic and evolving visuals, soundscapes, and interactive experiences. For example, machine learning can be used to generate procedural landscapes, simulate natural phenomena, or create adaptive music compositions. This blend of creativity and technology is empowering artists to push the boundaries of what is possible in digital art, creating immersive and ever-changing experiences for audiences."
    },
    {
        "slug": "generative-art-and-ai",
        "image": "generative_art.jpg",
        "author": "Xuzmonomi", 
        "date": date(2023, 5, 30),
        "title": "Generative Art and AI: A New Frontier",
        "excerpt": "Generative art is being transformed by AI, offering artists new ways to create complex and dynamic artworks.",
        "content": "Generative art, which involves creating art through algorithmic processes, is being revolutionized by the incorporation of AI. Artists are now using AI to design algorithms that can produce intricate and dynamic artworks, often with minimal human intervention. AI can analyze patterns, learn from data, and generate new and unique designs that evolve over time. This allows for the creation of art that is not only visually stunning but also endlessly variable. AI-driven generative art can produce everything from abstract patterns to realistic images, providing artists with a powerful tool to explore new creative possibilities and push the boundaries of traditional art forms."
    },
    {
        "slug": "ai-enhanced-digital-interactions",
        "image": "digital_interactions.jpg",
        "author": "Xuzmonomi", 
        "date": date(2024, 1, 18),
        "title": "Enhancing Digital Interactions with AI",
        "excerpt": "AI is enhancing digital interactions by creating more responsive and immersive experiences in interactive art and media.",
        "content": "Artificial Intelligence is playing a crucial role in enhancing digital interactions, particularly in the realm of interactive art and media. By incorporating AI, artists and developers can create experiences that are more responsive and immersive. AI can process real-time data from user interactions and adapt the digital environment accordingly. This can include changes in visual elements, audio responses, or even narrative directions based on user behavior. The result is a more engaging and personalized experience for the audience. AI-enhanced digital interactions are being used in various applications, from interactive museum exhibits to immersive virtual reality environments, making digital art and media more dynamic and interactive than ever before."
    },
    {
        "slug": "ai-art-in-installations",
        "image": "ai_installations.jpg",
        "author": "Xuzmonomi", 
        "date": date(2023, 7, 22),
        "title": "AI Art in Modern Installations",
        "excerpt": "AI is being integrated into modern art installations, creating interactive and evolving art pieces that engage viewers in new ways.",
        "content": "The integration of AI into modern art installations is creating new opportunities for artists to engage viewers in innovative ways. AI-powered installations can analyze and respond to viewer interactions, creating art that evolves in real time. For example, an AI installation might change its visual patterns or audio output based on the movements or emotions of viewers. This creates a dynamic and interactive experience that is unique to each participant. AI can also generate new content for installations, ensuring that the art remains fresh and engaging over time. By blending AI with traditional art forms, artists are creating installations that push the boundaries of what is possible in the art world."
    },
    {
        "slug": "ai-creative-tools",
        "image": "ai_tools.jpg",
        "author": "Xuzmonomi", 
        "date": date(2022, 6, 15),
        "title": "AI Tools for Creative Professionals",
        "excerpt": "AI tools are revolutionizing the creative industry, providing professionals with powerful resources to enhance their work.",
        "content": "AI tools are becoming indispensable in the creative industry, offering professionals powerful resources to enhance their work. These tools can assist in various creative processes, from generating visual content to composing music or writing text. For example, AI-powered design software can create intricate patterns, suggest color schemes, or even generate entire layouts based on user input. In music, AI can compose melodies, harmonize tracks, and produce unique soundscapes. Writers can use AI to generate ideas, draft content, and refine their prose. These tools are not just about automation but also about expanding creative possibilities, allowing professionals to experiment with new ideas and push their work to new heights."
    },
    {
       "slug": "progressive-generation-algorithm",
       "image": "picture.jpg",
       "author": "Xuzmonomi", 
       "date": date(2021, 7, 21),
       "title": "Procedural Generation Algorithm",
       "excerpt": """Procedural generation is the future of gaming open-world multiplayer online gaming. Instead of finite maps, AI could generate seamless expanses.""",
       "content": """Procedural generation algorithms have revolutionized the landscape of gaming and digital art. By leveraging AI, developers can create expansive, unique environments that evolve and adapt in real-time. This not only enhances player immersion but also opens new avenues for storytelling and game mechanics. Imagine exploring a game world that is never the same twice, where each player's journey is uniquely their own. This technology also reduces development time and costs, allowing smaller studios to produce content-rich experiences. As AI continues to advance, the potential applications of procedural generation in gaming and beyond are virtually limitless.""",
    },
    {
       "slug": "creative-coding-and-installations",
       "image": "installations.jpg",
       "author": "Xuzmonomi", 
       "date": date(2022, 8, 30),
       "title": "Creative Coding in Art Installations",
       "excerpt": """Creative coding is transforming art installations by enabling interactive, dynamic experiences that engage audiences on multiple levels.""",
       "content": """Creative coding has become a powerful tool in the realm of art installations, allowing artists to craft interactive and dynamic experiences that captivate audiences. By using programming languages and platforms like Processing, p5.js, and TouchDesigner, artists can create installations that respond to viewer movements, sounds, and other environmental factors. These interactive elements not only make the installations more engaging but also provide a deeper level of immersion. From light and sound installations that react to audience presence to data-driven art that visualizes complex datasets in real-time, creative coding is expanding the possibilities of what art can be and how it can interact with its environment and viewers.""",
    },
    {
       "slug": "ai-driven-visuals",
       "image": "visuals.jpg",
       "author": "Xuzmonomi", 
       "date": date(2023, 5, 5),
       "title": "AI-Driven Visual Art",
       "excerpt": """AI is revolutionizing visual art by generating stunning images and assisting artists in creating novel visual experiences.""",
       "content": """AI-driven visual art is at the forefront of contemporary digital art, harnessing the power of machine learning to create stunning and often unexpected imagery. Tools like neural networks can analyze and replicate artistic styles, generating new works that blend elements from various sources. Artists can use these AI tools to explore new visual aesthetics, combining their creative intuition with the computational power of AI to push the boundaries of traditional art forms. From generating hyper-realistic portraits to creating abstract pieces that challenge the viewer's perception, AI is proving to be a valuable collaborator in the artistic process, opening up new possibilities for visual expression.""",
    },
]

def get_date(item):
    return item["date"]

def home(request): 
    sorted_posts = sorted(articles, key=get_date, reverse=True)
    latest_posts = sorted_posts[:3]
    return render(request, "home/index.html",  {
        "posts": latest_posts
    })

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")
