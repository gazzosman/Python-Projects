const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");

if (navToggle && navLinks) {
  navToggle.addEventListener("click", () => {
    const isOpen = navToggle.getAttribute("aria-expanded") === "true";
    navToggle.setAttribute("aria-expanded", String(!isOpen));
    navLinks.classList.toggle("open", !isOpen);
  });

  navLinks.addEventListener("click", (event) => {
    if (event.target.matches("a")) {
      navToggle.setAttribute("aria-expanded", "false");
      navLinks.classList.remove("open");
    }
  });
}

const printButton = document.querySelector("#print-resume");
if (printButton) {
  printButton.addEventListener("click", () => window.print());
}

const year = document.querySelector("#year");
if (year) {
  year.textContent = new Date().getFullYear();
}
