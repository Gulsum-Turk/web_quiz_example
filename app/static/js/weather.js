let istanbul = ` <a class="weatherwidget-io" href="https://forecast7.com/tr/41d0128d98/istanbul/" data-label_1="İSTANBUL" data-label_2="Hava Durumu" data-theme="original" >İSTANBUL Hava Durumu</a>
<script>
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
</script>`

let ankara = `<a class="weatherwidget-io" href="https://forecast7.com/tr/39d9332d86/ankara/" data-label_1="ANKARA" data-label_2="Hava Durumu" data-theme="original" >ANKARA Hava Durumu</a>
<script>
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
</script>`

let izmir = `<a class="weatherwidget-io" href="https://forecast7.com/tr/38d4227d14/izmir/" data-label_1="İZMIR" data-label_2="Hava Durumu" data-theme="original" >İZMIR Hava Durumu</a>
<script>
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
</script>`

let bursa = `<a class="weatherwidget-io" href="https://forecast7.com/tr/40d1929d06/bursa/" data-label_1="BURSA" data-label_2="Hava Durumu" data-theme="original" >BURSA Hava Durumu</a>
<script>
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
</script>`

let antalya = `<a class="weatherwidget-io" href="https://forecast7.com/tr/36d9030d71/antalya/" data-label_1="ANTALYA" data-label_2="Hava Durumu" data-theme="original" >ANTALYA Hava Durumu</a>
<script>
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
</script>`

let diyarbakir = `<a class="weatherwidget-io" href="https://forecast7.com/en/37d9240d21/diyarbakir/" data-label_1="DIYARBAKIR" data-label_2="WEATHER" data-theme="original" >DIYARBAKIR WEATHER</a>
<script>
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
</script>`

        
document.addEventListener("DOMContentLoaded", function() {
    var weatherArea = document.getElementById("weatherArea");
    // Dropdown menüsünden seçilen şehre göre hava durumu bilgisini al ve göster
    var dropdownItems = document.querySelectorAll(".dropdown-item");
    dropdownItems.forEach(function(item) {
        item.addEventListener("click", function(event) {
            event.preventDefault(); // Sayfa yenilenmesini önle
            var city = item.innerText;
            switch (city) {
                case "İstanbul":
                    weatherArea.innerHTML = istanbul;
                    break;
                case "Ankara":
                    weatherArea.innerHTML = ankara;
                    break;
                case "İzmir":
                    weatherArea.innerHTML = izmir;
                    break;
                case "Antalya":
                    weatherArea.innerHTML = antalya;
                    break;
                case "Bursa":
                    weatherArea.innerHTML = bursa;
                    break;
                case "Diyarbakır":
                    weatherArea.innerHTML = diyarbakir;
                    break;
                default:
                    // Bilinmeyen hava durumu
                    weatherArea.innerHTML = "<p>Bilinmeyen şehir</p>";
                    break;
            }
            var script = document.createElement('script');
            script.src = 'https://weatherwidget.io/js/widget.min.js';
            script.async = true;
            document.body.appendChild(script);
        });
    });
});



