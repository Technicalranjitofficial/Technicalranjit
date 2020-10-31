
/* ========================================================
 Form Process
 * ========================================================*/

//On blur Form Validation events Executes only After failure of Submittion

var submit=false;  //Initially turns off on blur javascript event handlers

$('#name').on('blur', function () {
    'use strict';
    if(submit===true) {
        var select_name = $(this);
        var name = select_name.val();
        if (name === '') {
            if (!document.getElementById("name-message").hasChildNodes()) {
                $('#name-message').append("<p id='append_name' class='highlight'>Name cannot be blank</p>");
            }
        }
        else {
            remove_node("name-message","#append_name");
        }
    }
});
$('#email').on('blur', function () {
    'use strict';
    if(submit===true) {
        var select_email = $(this);
        var email = select_email.val();
        if (email === '') {
            if (!document.getElementById("email-message").hasChildNodes()) {
                $('#email-message').append("<p id='append_email' class='highlight'>Email cannot be blank</p>");
            }
        }
        else {
            remove_node("email-message","#append_email");
        }
    }
});
$('#message').on('blur', function () {
    'use strict';
    if(submit===true) {
        var select_message = $(this);
        var message = select_message.val();
        if (message === '') {
            if (!document.getElementById("text-message").hasChildNodes()) {
                $('#text-message').append("<p id='append_text' class='highlight'>Please Provide us a message.if any!</p>");
            }
        }
        else {
            remove_node("text-message","#append_text");
        }
    }
});
$('#result').on('blur', function () {
    'use strict';
    if(submit===true) {
        var select_captcha = $(this);
        var result = select_captcha.val();
        if (result === '') {
            if (!document.getElementById("captcha-message").hasChildNodes()) {
                $('#captcha-message').append("<p id='append_captcha' class='highlight'>Please fill this field for security check</p>");
            }
        }
        else {
            remove_node("captcha-message","#append_captcha");
        }
    }
});
$('#sunsetContactForm').on('submit',function (e) {
    'use strict';

    //On Submit Form Validation events
    var select_name=$('#name');
    var select_email=$('#email');
    var select_message=$('#message');
    var select_captcha=$('#result');
    if(!select_name.val() || !select_email.val() ||!select_message.val() ||!select_captcha.val()) { //If any of the field is empty
        var name = select_name.val();
        if (name === '') {
            if (!document.getElementById("name-message").hasChildNodes()) {
                $('#name-message').append("<p id='append_name' class='highlight'>Name cannot be blank</p>");
            }
            e.preventDefault();
        }

        var email = select_email.val();
        if (email === '') {
            if (!document.getElementById("email-message").hasChildNodes()) {
                $('#email-message').append("<p id='append_email' class='highlight'>Email cannot be blank</p>");
            }
            e.preventDefault();
        }

        var message = select_message.val();
        if (message === '') {
            if (!document.getElementById("text-message").hasChildNodes()) {
                $('#text-message').append("<p id='append_text' class='highlight'>Please Provide us a message.if any!</p>");
            }
            e.preventDefault();
        }

        var result = select_captcha.val();
        if (result === '') {
            if (!document.getElementById("captcha-message").hasChildNodes()) {
                $('#captcha-message').append("<p id='append_captcha' class='highlight'>Please fill this field for security check</p>");
            }
            e.preventDefault();
        }

        submit=true;
        return;     //Does not proceed if any of the fields is empty
    }
    /* Step 2. Recieve Random data from index.html due to step 1 */

    var rand_check1  =   parseInt($("#data1").data('toggle'));
    var rand_check2  =   parseInt($("#data2").data('toggle'));

    var answer= parseInt(select_captcha.val());

    if(answer!==(rand_check1+rand_check2)){
        e.preventDefault();
        location.reload();
    }
});

/*======================================
        Captcha
========================================*/

    /* Step 1. Input Random data to index.html */
var rand_num_1 = Math.ceil((Math.random())*10);
var rand_num_2 = Math.ceil((Math.random())*10);

$('#captcha').append('<label>'+rand_num_1+'+'+rand_num_2+'='+'</label>');

$(document).ready(function () {
    'use strict';
     $("#data1").attr("data-toggle", rand_num_1);       //Append Data Attribute
     $("#data2").attr("data-toggle", rand_num_2);       //Append Data Attribute

});