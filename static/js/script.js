const data=document.getElementById("capitulos-data").textContent;// Obtener el contenido del script con id capitulos-data
const capitulos=JSON.parse(data); // Convertir el texto en un objeto JSON

const audio=document.getElementById("player");
const infoCapitulo=document.getElementById("info-capitulo");
const botonEncender=document.getElementById("boton-encender-radio");
const botonAdelantar=document.getElementById("boton-adelantar-capitulos" );
const botonApagar=document.getElementById("boton-apagar-radio");
const botonRetroceder=document.getElementById("boton-retroceder-capitulos");

let episodioActual=0; // Variable para llevar el control del episodio actual

audio.volume = 1.0; // Establecer el volumen del audio al 50%

// Función para obtener el episodio actual
function reproducir(episodioActual) {
    const cap = capitulos[episodioActual];
    audio.src = `/static/audios/novelas/${cap.archivo}`;
    audio.play(); // Siempre reproduce el nuevo capítulo
    infoCapitulo.textContent = `${cap.id}-${cap.title}`;
   
}

botonEncender.addEventListener("click", () => {
    episodioActual = 0; // Reiniciar al primer episodio
    reproducir(episodioActual); // Reproducir el primer episodio
});

botonApagar.addEventListener("click", () => {
    if (audio.paused){
        audio.play(); // Reproducir el audio si está pausado
    }else {
        audio.pause(); // Pausar el audio si está reproduciendo
    }

});
botonAdelantar.addEventListener("click",() => {
    episodioActual++; // Incrementar el episodio actual
    if (episodioActual <= capitulos.length-1) {
        reproducir(episodioActual);
        console.log(`Reproduciendo episodio ${episodioActual + 1}: ${capitulos[episodioActual].title}`);
    }
    });
 
botonRetroceder.addEventListener("click",() => {
    episodioActual--; // Decrementar el episodio actual
    if (episodioActual >= 0) {
        reproducir(episodioActual);
    }else{
        episodioActual=0;
        reproducir(episodioActual); // Reiniciar al primer episodio si se intenta retroceder más allá del primero
        
    }
    });