feather.replace();

// DARK MODE
const toggle = document.getElementById("dark-toggle");
toggle.addEventListener("click", () => {
    document.documentElement.classList.toggle("dark");
});

// LIVE TEXT PREVIEW
document.getElementById("personal-text").addEventListener("input", e => {
    document.getElementById("text-overlay").textContent =
      e.target.value || "YOUR NAME";
});

// COLOR PICKER
document.getElementById("cover-color").addEventListener("input", e => {
    document.getElementById("passport-preview").style.backgroundColor = e.target.value;
});

// PINTEREST URL IMAGE
document.getElementById("pinterest-url").addEventListener("change", e => {
    const url = e.target.value;
    if (url.trim().length > 5) {
        document.getElementById("passport-preview").src = url;
    }
});

// FILE UPLOAD
document.getElementById("image-upload").addEventListener("change", e => {
    const file = e.target.files[0];
    if (file) {
      document.getElementById("passport-preview").src = URL.createObjectURL(file);
    }
});
