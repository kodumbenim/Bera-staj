document.querySelector("button").addEventListener("click", function (e) {
  e.preventDefault(); 

  const email = document.querySelector("#email").value;
  const password = document.querySelector("#password").value;

  fetch("/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      email: email,
      password: password
    })
  })
    .then(async res => {
      const text = await res.text(); 
      try {
        const data = JSON.parse(text); 
        if (data.status === "success") {
          alert("Giriş başarılı!");
        } else {
          alert(data.message || "Bilinmeyen hata");
        }
      } catch (err) {
        console.error("Sunucudan gelen bozuk veri:", text);
        alert("Sunucudan beklenmeyen yanıt alındı.");
      }
    })
    .catch(err => {
      console.error("İstek sırasında hata oluştu:", err.message);
      alert("Sunucuya bağlanılamadı.");
    });
});
