function validateNum(e){
    tecla = (document.all) ? e.keyCode : e.which;

    //Tecla de retroceso para borrar, siempre la permite
    if (tecla==8){
        return true;
    }
        
    // Patron de entrada, en este caso solo acepta numeros
    patron =/[0-9]/;
    tecla_final = String.fromCharCode(tecla);
    return patron.test(tecla_final);
};

function validateString(e){
    tecla = (document.all) ? e.keyCode : e.which;

    //Tecla de retroceso para borrar, siempre la permite
    if (tecla==200){
        return true;
    }
        
    // Patron de entrada, en este caso solo acepta numeros
    //patron =/[A-Za-zñÑ]/;
    patron = /^[\\p{L} .'-, A-Za-zñÑ]+$/
    tecla_final = String.fromCharCode(tecla);
    return patron.test(tecla_final);
};

function validateEmail(e){
    tecla = (document.all) ? e.keyCode : e.which;

    //Tecla de retroceso para borrar, siempre la permite
    if (tecla==8){
        return true;
    }
        
    // Patron de entrada, en este caso solo acepta numeros
    patron = /\D/;
    //patron =/\S+@\S+\.\S+/;
    tecla_final = String.fromCharCode(tecla);
    return patron.test(tecla_final);
};

function validateEmail2(e) {
    tecla = (document.all) ? e.keyCode : e.which;
    //Tecla de retroceso para borrar, siempre la permite
    if (tecla==200){
        return true;
    }
    patron = /^(([^<>()[]\.,;:s@"]+(.[^<>()[]\.,;:s@"]+)*)|(".+"))@(([[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}])|(([a-zA-Z-0-9]+.)+[a-zA-Z]{2,}))$/igm;
    tecla_final = String.fromCharCode(tecla);

    return patron.test(tecla_final);
}

function validateInputs() {
    console.log('validateInputs')
    //Validación match de contraseñas
    var pass1 = document.getElementById("password").value;
    var pass2 = document.getElementById("password2").value;
    var ok = true;
    if (pass1 != pass2) {
        document.getElementById("password").style.borderColor = "#E34234";
        document.getElementById("password2").style.borderColor = "#E34234";
        Materialize.toast('Las contraseñas no coinciden', 4000, 'red')
        ok = false;
    } else {
        document.getElementById("password").style.borderColor = "#4CAF50";
        document.getElementById("password2").style.borderColor = "#4CAF50";
    }

    return ok;
}

function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    var weekday = new Array(7);
    weekday[0]=  "Domingo";
    weekday[1] = "Lunes";
    weekday[2] = "Martes";
    weekday[3] = "Miércoles";
    weekday[4] = "Jueves";
    weekday[5] = "Viernes";
    weekday[6] = "Sábado";
    var day = weekday[today.getDay()];
    var dayNumber = today.getDate();
    var months = new Array(12);
    months[0]=  "Enero";
    months[1] = "Febrero";
    months[2] = "Marzo";
    months[3] = "Abril";
    months[4] = "Mayo";
    months[5] = "Junio";
    months[6] = "Julio";
    months[7] = "Agosto";
    months[8] = "Setiembre";
    months[9] = "Octubre";
    months[10] = "Noviembre";
    months[11] = "Diciembre";
    var month = months[today.getMonth()];
    var year = today.getFullYear();

    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('hour').innerHTML = h + ":" + m + ":" + s;
    document.getElementById('date').innerHTML = day + " " + dayNumber + " de " + month + ", " + year;
    var t = setTimeout(startTime, 500);
}

function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

$(document).ready(function() {
    $('select').material_select();
    //llenar los progress bar

    $('.componentprogress').each(function() {
		porcentaje = document.getElementById("status"+this.id).innerHTML
    	var elem = document.getElementById("componentbar"+this.id); 
        console.log(porcentaje);
        elem.style.width = porcentaje.replace(",",".");
    	var porcentajeEntero = parseInt(porcentaje.replace("%", ""));
    	if(porcentajeEntero<50)
    		elem.style.backgroundColor = "#F44336";
    	else if(porcentajeEntero>=50 && porcentajeEntero<70)
    		elem.style.backgroundColor = "#FFEB3B";
	});


    //VALIDACIONES DE INPUTS
    
    //Validación de emails
    $('form input[name="email"]').blur(function () {
        var email = $(this).val();
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/igm;
        if (re.test(email)) {
            $('.msg').hide();

            //Validación de email duplicado
            console.log('else')
            $.ajax({
                type:'POST',
                url:'{% url "employees:search_mail_employee" %}',
                data:{
                    email:email,
                    csrfmiddlewaretoken:'{{ csrf_token }}',
                },
                success: function(data){
                    console.log("regrese...data:")
                    console.log(data)

                    //document.getElementById("email").style.borderColor = "#E34234";
                    console.log("termine..")
                },
                /**error: function(){
                    console.log("error")
                    document.getElementById("email").style.borderColor = "#4CAF50";
                    $('.msg').hide();
                    $('.error-duplicate').show();
                    ok = false;
                }**/
            });
            
        } else {
            $('.msg').hide();
            $('.error').show();
        }
    });
});
