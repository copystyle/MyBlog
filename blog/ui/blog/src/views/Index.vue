<template lang="html">
  <div class="index">
    <header class="header">
        <div class="container">
            <nav class="navbar navbar-inverse" role="navigation">
                <div class="navbar-header">
                    <p class="navbar-brand scroll-top logo"><b>CopyStyle' Domain</b></p>
                </div>
                <div id="main-nav" class="collapse navbar-collapse">
                    <ul class="nav navbar-nav" id="mainNav">
                        <li><a href="https://github.com/copystyle" class="scroll-link">Github</a></li>
                        <li><a href="https://www.zhihu.com/people/copystyle/activities" class="scroll-link">知乎</a></li>
                        <li><a href="https://www.jianshu.com/users/59ccf21c7374/timeline" class="scroll-link">简书</a></li>
                    </ul>
                </div>
            </nav>
        </div>
    </header>
    <div id="#top"></div>
    <section id="home">
        <div class="banner-container">
            <img src="../assets/images/banner-bg.jpg" alt="banner" />
            <div class="container banner-content">
                <div id="da-slider" class="da-slider">
                    <div class="da-slide">
                        <h2>Webdesigner</h2>
                        <p>Amazing free responsive website for free, enjoy!!!</p>
                        <div class="da-img"></div>
                    </div>
                    <div class="da-slide">
                        <h2>UX/UI Developer</h2>
                        <p>I develop website using Bootstrap front-end framework..</p>
                        <div class="da-img"></div>
                    </div>
                    <div class="da-slide">
                        <h2>HTML5/CSS3</h2>
                        <p>HTML5 is a markup language used for structuring and presenting Web.</p>
                        <div class="da-img"></div>
                    </div>
                    <div class="da-slide">
                        <h2>JavaScript/jQuery</h2>
                        <p>jQuery: Write Less, Do More...</p>
                        <div class="da-img"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section id="introText">
        <div class="container">
            <div class="text-center">
            <h1>I am a novice programmer, eager to be a Geek.</h1>
              <p>I am a software engineer based in Shanghai, China.</p>
              <p>In my free time, I am excited to explore anything I am interested or related to my work.</p>
              <p>They can always help me to improve myself, open my eyes and get ready to the near future.</p>
            </div>
        </div>

    </section>
    <section id="aboutUs" class="secPad">
        <div class="container">
            <div class="heading text-center">
                <h2>This is CopyStyle</h2>
            </div>
            <div class="row">
                <div class="col-md-4 text-center tileBox">
                    <div class="txtHead"><i class="fa fa-desktop"></i>
                    <h3>Python</h3></div>
                </div>
                <div class="col-md-4 text-center tileBox">
                    <div class="txtHead"><i class="fa fa-lightbulb-o"></i>
                    <h3>JavaScript</h3></div>
                </div>
                <div class="col-md-4 text-center tileBox">
                    <div class="txtHead"><i class="fa fa-css3"></i>
                    <h3>HTML5/CSS3</h3></div>
                </div>
            </div>
        </div>
    </section>
    <section id="quote" class="bg-parlex">
        <div class="parlex-back">
            <div class="container secPad text-center">
              <h2>‘It works on my machine!’</h2>
            </div>
        </div>
    </section>
    <a href="#top" class="topHome"><i class="fa fa-chevron-up fa-2x"></i></a>
    <canvas width="1920" height="950"></canvas>
  </div>
</template>

<script>
import '../assets/css/bootstrap.min.css'
import '../assets/css/isotope.css'
import '../assets/css/jquery.fancybox.css'
import '../assets/css/da-slider.css'
import '../assets/css/owl.carousel.css'
import '../assets/css/styles.css'
import '../assets/css/font-awesome.min.css'
import '../assets/css/font-awesome.css'
document.title = 'CopyStyle'
</script>

<style media="screen" scoped>
  h1, h2 {
    position: relative;
  }
  canvas {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
  }
</style>
