let clues = [];

function startGame() {
    document.getElementById("start-screen").style.display = "none";
    document.getElementById("game-screen").style.display = "block";
}
function investigateRoom() {
    if (clues.length === 0) { 
        clues.push("KirmiziIplik");
        alert("Odayi dikkatlice incelediniz ve bir tane yerde kirmizi iplik buldunuz. \n\n" +
    "Ve bu iplik, olay yerinde birinin bulunmuş olabileceğini gösteriyor.");
} else if (clues.length === 1) {
    clues.push("AyakkabiIzleri");
    alert(" Bu odayi dikkatlice incelediniz ve yerde ayakkabi izleri buldunuz. \n\n" +
    "Bu izler, olay yerinde birinin bulunmuş olabileceğini gösteriyor.");
} else if (clues.length === 2) {
    clues.push("GizemliNot");
    alert("Masanın üzerinde gizemli bir not buldun!\n\n" +
            "Notta şöyle yazıyor:\n" +
            "\"Bu tablo asla bulunamayacak.\"\n\n" );
} else if (clues.length === 3) { clues.push("Kamera kaydı");
    alert(
            "Güvenlik odasında bir kamera kaydı buldun!\n\n" +
            "Kayıtta galerinin yakınında şüpheli bir kişi görünüyor.\n\n" +
            "Kanıt çantana eklendi!");
} else {
    alert("Odayı tekrar incelediniz. Daha fazla ipucu bulamadınız.");
    }
}
function showSuspects() {
    document.getElementById("suspect-list").style.display = "block";
    alert("Şüpheliler:\n\n" +
        "1. Ahmet | Galeri Sahibi \n" +
        "2. Ayşe | Sanat Danismani \n" +
        "3. Emre | Güvenlik Görevlisi \n" +
        "4. Deniz | Temizlik Görevlisi \n" +
        "5. Mehmet | Koleksiyoner \n" 
    );
    }

 function questionSuspect(name) {

    if (name === "Ahmet") {
         alert( "Ahmet, Galeri Sahibi:\n\n" +
        "Tablonun kaybolduğu sırada ofisimdeydim.\n\n" +
            "\"Galerinin anahtarı sadece bende bulunuyordu.\"");
    } else if (name === "Ayşe") {
        alert("Ayşe, Sanat Danismani:\n\n" +
            "Tablo benim için çok değerliydi.\"\n\n" +
            "\"Ama onu neden çalayım ki?\"");
    } else if (name === "Emre") {
            alert("Emre, Güvenlik Görevlisi:\n\n" +
                "\" O gece kameralari kontrol ediyordum ve odadaydim \"\n\n" +
                "\"Ama tablonun kaybolduğunu fark etmedim.\"");
            let choice = window.prompt ("Emre`ye inaniyor musunuz gerçekten ? Emre`nin ifadesini hangi kanitla sorgulamak istiyorsun?\n\n" +
                " 1. KirmiziIplik \n " +
                " 2. AyakkabiIzleri \n " +
                " 3. GizemliNot \n " +
                " 4. Kamera kaydı"
            ); 
            if (choice === "1" && clues.includes("KirmiziIplik")) {
                alert("Bu kanıt Emre'nin ifadesiyle doğrudan bağlantılı görünmüyor.");
            } else if (choice === "2" && clues.includes("AyakkabiIzleri")) {
                alert("Evet o gece oralarda gezindim ama tablonun kaybolduğunu fark etmedim.");
            } else if (choice === "3" && clues.includes("GizemliNot")) {
                alert("Bu notu ben yazmadım. Ben sadece güvenlik görevlisiyim.");
            } else if (choice === "4" && clues.includes("Kamera kaydı")) {
                alert("Evet, o gece kameralarda şüpheli bir kişi vardı ama ben onu tanımıyorum.");
            } else {
                alert("Geçersiz seçim , bir sonraki sorgulamada tekrar denemelisin ona yaklastin ");
            }
        }
        else if (name === "Deniz") {
        alert("Deniz, Temizlik Görevlisi:\n\n" +
            "\"O gece temizlik yapıyordum.\"\n\n" +
            "\"Ama tablonun kaybolduğunu fark etmedim.\"");
    } else if (name === "Mehmet") {
        alert("Mehmet, Koleksiyoner:\n\n" +
            "\"Tabloyu çok beğeniyorum.\"\n\n" +
            "\"Ama onu çalmam için bir sebep yok.\"");
        }
 }
function showClues() {
    if (clues.length === 0) {
        alert("Henüz hiçbir ipucu bulunamadı.");
    } else {
       let evidenceList = "Bulunan İpuçları:\n\n";
       for (let i = 0; i < clues.length; i++) {
           evidenceList += "- " + clues[i] + "\n";
       }
       alert(evidenceList);
    }
}

