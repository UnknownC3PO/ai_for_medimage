$(document).ready(function () {
    // Init
    $('.image-section_1').hide();
    $('.loader_1').hide();
    $('#result_1').hide();

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview_1').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview_1').hide();
                $('#imagePreview_1').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload_1").change(function () {
        $('.image-section_1').show();
        $('#btn-predict_1').show();
        $('#result_1').text('');
        $('#result_1').hide();
        readURL(this);
    });

    // Predict
    $('#btn-predict_1').click(function () {
        var form_data = new FormData($('#upload-file_1')[0]);

        // Show loading animation
        $(this).hide();
        $('.loader_1').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predictAnything',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader_1').hide();
                $('#result_1').fadeIn(600);
                $('#result_1').text(' Result:  ' + data);
                console.log('Success!');
            },
        });
    });
});
