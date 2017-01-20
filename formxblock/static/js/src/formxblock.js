/* Javascript for FormXBlock. */
function FormXBlock(runtime, element) {

    function changeText(result) {
        $('#form-container', element).hide(1000);

        $('#confirm-dialog', element).show(1000); 
    }

    function setCount(result) {
        $('#contador', element).html(result.count); 
    }

    $('.send', element).click(function(eventObject) {
        var form = {
            datos: []
        }
        var inputs = $(".input-form");
        for (var i = 0; i < inputs.length; i++) {
            form.datos.push($(inputs[i]).val());
        }
        saveData(form);
    });

    $('.view_data', element).click(function(eventObject) {
        var handlerUrl = runtime.handlerUrl(element, 'get_count');
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world"}),
            success: setCount
        });

        $('#form-container', element).hide(1000);
        $('#display-data', element).show(1000);
    });

    $('#back_to_form', element).click(function(eventObject) {
        $('#display-data', element).hide();
        $('#form-container', element).show();
    });

    function saveData(jsonObj) {
        var handlerUrl = runtime.handlerUrl(element, 'test_func');
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify(jsonObj),
            success: changeText
        });
    }

    $(function ($) {
        /* Here's where you'd do things on page load. */
        $('#confirm-dialog').hide();
        $('#user-alert').hide();
        $('#display-data').hide(); 
    });
}
