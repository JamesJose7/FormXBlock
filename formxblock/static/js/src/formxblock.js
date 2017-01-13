/* Javascript for FormXBlock. */
function FormXBlock(runtime, element) {

    function changeText(result) {
        //$('.count', element).text(result.count);
        /*$('.name', element).text("this should appear");
        $('#bibliografia', element).text(result.nombre[0]);*/
        //alert("QUE HUBO");
        $('#form-container', element).hide(2000);
        //$('#usuario', element).text(result.tookSurvey);
        
        //$('#user-alert', element).show(2000);
        
        $('#confirm-dialog', element).show(2000);
        
    }

    function test(result) {

    }

    //var handlerUrl = runtime.handlerUrl(element, 'test_func');

    $('.send', element).click(function(eventObject) {
        var form = {
            datos: []
        }
        //form.datos.push($('#usuario').val());
        var inputs = $(".input-form");
        for (var i = 0; i < inputs.length; i++) {
            form.datos.push($(inputs[i]).val());
        }
        saveData(form);

        /*$.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({tookSurvey: "False"}),
            success: changeText
        });*/
    });

    function saveData(jsonObj) {
        var handlerUrl = runtime.handlerUrl(element, 'test_func');
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify(jsonObj),
            success: changeText(jsonObj)
        });
    }

    $(function ($) {
        /* Here's where you'd do things on page load. */
        $('#confirm-dialog').hide();
        $('#user-alert').hide();
    });
}
