<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Swayam Mansingh | Portfolio</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>

:root{
    --bg:#080b14;
    --card:rgba(255,255,255,.08);
    --primary:#00e5ff;
    --secondary:#7c3aed;
    --text:#ffffff;
}

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
    scroll-behavior:smooth;
}

body{
    background:var(--bg);
    color:var(--text);
    overflow-x:hidden;
}

/* Animated Background */

body::before{
    content:"";
    position:fixed;
    width:600px;
    height:600px;
    background:var(--secondary);
    filter:blur(180px);
    opacity:.2;
    top:-200px;
    left:-200px;
    z-index:-1;
}

body::after{
    content:"";
    position:fixed;
    width:600px;
    height:600px;
    background:var(--primary);
    filter:blur(180px);
    opacity:.15;
    right:-200px;
    bottom:-200px;
    z-index:-1;
}

nav{
    position:fixed;
    width:100%;
    top:0;
    z-index:100;
    backdrop-filter:blur(20px);
    background:rgba(0,0,0,.2);
}

.nav-container{
    width:90%;
    margin:auto;
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:20px 0;
}

.logo{
    font-size:1.5rem;
    font-weight:700;
    color:var(--primary);
}

nav ul{
    display:flex;
    list-style:none;
    gap:25px;
}

nav a{
    text-decoration:none;
    color:white;
    transition:.3s;
}

nav a:hover{
    color:var(--primary);
}

.hero{
    min-height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    text-align:center;
    padding:20px;
}

.hero-content{
    max-width:800px;
}

.hero h1{
    font-size:5rem;
    margin-bottom:15px;
}

.hero h1 span{
    color:var(--primary);
}

.hero p{
    color:#cbd5e1;
    margin-bottom:30px;
}

.buttons{
    display:flex;
    justify-content:center;
    gap:15px;
    flex-wrap:wrap;
}

.btn{
    padding:14px 30px;
    border-radius:50px;
    text-decoration:none;
    font-weight:600;
    transition:.3s;
}

.btn-primary{
    background:var(--primary);
    color:black;
}

.btn-secondary{
    border:1px solid rgba(255,255,255,.2);
    color:white;
}

.btn:hover{
    transform:translateY(-4px);
}

section{
    padding:100px 10%;
}

.section-title{
    text-align:center;
    font-size:2.5rem;
    margin-bottom:60px;
    color:var(--primary);
}

.glass{
    background:var(--card);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,.1);
    border-radius:20px;
}

.about{
    padding:40px;
    text-align:center;
}

.about p{
    max-width:800px;
    margin:auto;
    color:#cbd5e1;
}

.skills{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:15px;
}

.skill{
    padding:12px 22px;
    border-radius:30px;
    background:var(--card);
    border:1px solid rgba(255,255,255,.1);
}

.projects{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:25px;
}

.project-card{
    padding:25px;
    transition:.4s;
}

.project-card:hover{
    transform:translateY(-10px);
}

.project-card h3{
    color:var(--primary);
    margin-bottom:10px;
}

.project-card p{
    color:#cbd5e1;
}

.contact{
    text-align:center;
}

.contact a{
    color:var(--primary);
    text-decoration:none;
}

.socials{
    margin-top:25px;
    display:flex;
    justify-content:center;
    gap:20px;
}

.socials a{
    color:white;
    text-decoration:none;
    padding:10px 20px;
    border-radius:30px;
    background:var(--card);
}

footer{
    text-align:center;
    padding:30px;
    color:#94a3b8;
}

@media(max-width:768px){

.hero h1{
    font-size:3rem;
}

nav ul{
    display:none;
}

}

</style>
</head>
<body>

<nav>
    <div class="nav-container">
        <div class="logo">SM</div>

        <ul>
            <li><a href="#about">About</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </div>
</nav>

<section class="hero">

<div class="hero-content">

<h1>Swayam <span>Mansingh</span></h1>

<p>
Full Stack Developer • UI Designer • Tech Enthusiast
Building modern digital experiences with creativity and code.
</p>

<div class="buttons">
<a href="#projects" class="btn btn-primary">View Projects</a>
<a href="resume.pdf" class="btn btn-secondary" download>
Download Resume
</a>
</div>

</div>
</section>

<section id="about">

<h2 class="section-title">About Me</h2>

<div class="glass about">
<p>
I'm Swayam Mansingh, a passionate developer who loves creating
beautiful interfaces and scalable applications. I enjoy working
with web technologies, artificial intelligence, and innovative
digital products.
</p>
</div>

</section>

<section id="skills">

<h2 class="section-title">Skills</h2>

<div class="skills">

<div class="skill">HTML5</div>
<div class="skill">CSS3</div>
<div class="skill">JavaScript</div>
<div class="skill">React</div>
<div class="skill">Node.js</div>
<div class="skill">Express</div>
<div class="skill">MongoDB</div>
<div class="skill">Python</div>
<div class="skill">Git</div>
<div class="skill">UI/UX Design</div>

</div>

</section>

<section id="projects">

<h2 class="section-title">Featured Projects</h2>

<div class="projects">

<div class="glass project-card">
<h3>Nova AI</h3>
<p>
AI-powered virtual assistant capable of task automation,
content generation, and workflow optimization.
</p>
</div>

<div class="glass project-card">
<h3>EcoVision</h3>
<p>
Environmental analytics platform helping users track
their sustainability goals and carbon footprint.
</p>
</div>

<div class="glass project-card">
<h3>TaskFlow</h3>
<p>
Project management application with real-time
collaboration and smart productivity insights.
</p>
</div>

<div class="glass project-card">
<h3>CodeSphere</h3>
<p>
Collaborative coding platform supporting live editing,
version control integration, and team workspaces.
</p>
</div>

<div class="glass project-card">
<h3>SkyRoute</h3>
<p>
AI-driven travel planner that builds personalized
trip itineraries and recommendations.
</p>
</div>

<div class="glass project-card">
<h3>VisionX Analytics</h3>
<p>
Computer vision dashboard for image analysis,
object recognition, and business intelligence.
</p>
</div>

</div>

</section>

<section id="contact">

<h2 class="section-title">Contact</h2>

<div class="glass about contact">

<p>Email: swayam@example.com</p>

<div class="socials">
<a href="#">GitHub</a>
<a href="#">LinkedIn</a>
<a href="#">Twitter</a>
</div>

</div>

</section>

<footer>
© 2026 Swayam Mansingh • Crafted with HTML, CSS & Passion
</footer>

</body>
</html>
