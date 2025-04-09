<!DOCTYPE html><html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Store Vanii - Jasa Game</title>
  <link href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css"/>
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(to bottom right, #2e1a1a, #1a1a1a);
      color: #fdfdfd;
      transition: background 0.3s, color 0.3s;
      overflow-x: hidden;
    }
    body.light {
      background: linear-gradient(to bottom right, #fef3e2, #f6e7d7);
      color: #222;
    }
    header {
      padding: 1rem;
      background-color: #3e2723;
      text-align: center;
      color: #fdd835;
      animation: fadeSlideDown 1.5s ease;
    }
    body.light header {
      background-color: #fdd835;
      color: #3e2723;
    }
    h1, h2 { margin: 1rem 0; }
    section {
      padding: 2rem 1rem;
      max-width: 960px;
      margin: 0 auto;
      animation: fadeSlideUp 1s ease;
    }
    .toggle-theme {
      position: fixed;
      top: 1rem;
      right: 1rem;
      background: #fdd835;
      color: #3e2723;
      border: none;
      padding: 0.5rem 1rem;
      cursor: pointer;
      border-radius: 5px;
      transition: background 0.3s;
      z-index: 1000;
    }
    .toggle-theme:hover { background: #ffeb3b; }
    .floating-btn {
      position: fixed;
      bottom: 1rem;
      right: 1rem;
      display: flex;
      flex-direction: column;
      gap: 10px;
      z-index: 999;
    }
    .floating-btn a {
      background: #f06292;
      padding: 8px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 40px;
      height: 40px;
      box-shadow: 0 0 10px rgba(0,0,0,0.2);
    }
    .floating-btn img {
      width: 20px;
      height: 20px;
    }
    .swiper {
      width: 100%;
      padding: 20px 0;
    }
    .swiper-slide {
      background: rgba(255,255,255,0.08);
      border-radius: 15px;
      padding: 20px;
      text-align: center;
      margin: 0 10px;
    }
    .swiper-slide strong {
      display: block;
      margin-top: 10px;
      font-size: 14px;
    }
    body.light .swiper-slide {
      background: rgba(0,0,0,0.05);
    }
    @keyframes fadeSlideUp {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeSlideDown {
      from { opacity: 0; transform: translateY(-20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    #welcome-toast {
      position: fixed;
      top: 20px;
      left: 50%;
      transform: translateX(-50%);
      background: #ffccbc;
      color: #3e2723;
      padding: 1rem 2rem;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.2);
      opacity: 0;
      pointer-events: none;
      z-index: 9999;
      transition: opacity 0.5s;
    }
    #welcome-toast.show {
      opacity: 1;
      pointer-events: auto;
    }
    .play-music-btn {
      position: fixed;
      bottom: 1rem;
      left: 1rem;
      background-color: #f06292;
      color: white;
      border: none;
      border-radius: 20px;
      padding: 10px 20px;
      cursor: pointer;
      z-index: 999;
      box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
  </style>
</head>
<body>
  <div id="welcome-toast">Selamat datang di Store Vanii!</div>
  <button class="toggle-theme" onclick="toggleTheme()">Ganti Tema</button>
  <button class="play-music-btn" onclick="document.getElementById('bgmusic').play()">Putar Lagu</button>  <audio id="bgmusic">
    <source src="https://vgmsite.com/soundtracks/serial-experiments-lain-ost/igxwpzrcui/01.%20Duvet.mp3" type="audio/mpeg">
    Browser Anda tidak mendukung audio.
  </audio>  <header>
    <h1>Store Vanii</h1>
    <p>Jasa Game Profesional dan Terpercaya</p>
  </header>  <section data-aos="fade-up">
    <h2>Deskripsi</h2>
    <p>Kami menyediakan berbagai layanan game seperti joki, coaching, dan lainnya dengan layanan terbaik, aman, dan terpercaya.</p>
  </section>  <section data-aos="fade-up">
    <h2>Fitur Layanan</h2>
    <ul>
      <li>Joki Game Mobile dan PC</li>
      <li>Coaching dengan Pro Player</li>
      <li>Layanan Customer Support 24 Jam</li>
    </ul>
  </section>  <section data-aos="fade-up">
    <h2>Kontak & Pemesanan</h2>
    <p>Silakan hubungi kami melalui Telegram atau WhatsApp untuk pemesanan langsung.</p>
  </section>  <section id="testimoni" data-aos="fade-up">
    <h2>Testimoni Pelanggan</h2>
    <div class="swiper mySwiper">
      <div class="swiper-wrapper">
        <div class="swiper-slide">
          "Layanannya sangat cepat dan aman, saya berhasil naik rank dalam waktu singkat!"
          <strong>- Andi, Jakarta</strong>
        </div>
        <div class="swiper-slide">
          "Timnya sangat ramah dan profesional. Saya puas banget sama coaching-nya."
          <strong>- Rina, Surabaya</strong>
        </div>
        <div class="swiper-slide">
          "Harga terjangkau, layanan berkualitas. Sudah langganan di Store Vanii!"
          <strong>- Budi, Bandung</strong>
        </div>
        <div class="swiper-slide">
          "Support cepat dan hasil memuaskan. Recommended banget buat para gamer!"
          <strong>- Sinta, Makassar</strong>
        </div>
      </div>
      <div class="swiper-pagination"></div>
    </div>
  </section>  <div class="floating-btn">
    <a href="https://t.me/storevanii" target="_blank">
      <img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" alt="Telegram">
    </a>
    <a href="https://wa.me/6281234567890" target="_blank">
      <img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" alt="WhatsApp">
    </a>
    <a href="mailto:storevanii@gmail.com" target="_blank">
      <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="Email">
    </a>
  </div>  <script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>  <script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>  <script>
    AOS.init();

    const toggleTheme = () => {
      document.body.classList.toggle('light');
    }

    var swiper = new Swiper(".mySwiper", {
      effect: "slide",
      loop: true,
      grabCursor: true,
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
      autoplay: {
        delay: 5000,
      },
    });

    // Welcome toast
    window.addEventListener("DOMContentLoaded", () => {
      const toast = document.getElementById("welcome-toast");
      toast.classList.add("show");
      setTimeout(() => {
        toast.classList.remove("show");
      }, 4000);
    });
  </script></body>
</html>
