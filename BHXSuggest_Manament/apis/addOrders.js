$(document).ready(function() {
    $('#uploadButtonOrders').click(function() {
        var fileInput = $('#jsonFileOrders')[0];
        if (fileInput.files.length === 0) {
            alert("Hãy nhập file JSON");
            return;
        }
        var file = fileInput.files[0];
        var formData = new FormData();
        formData.append('file', file);
        uploadFile(formData);
    });

    function uploadFile(formData) {
        $('#uploadProcess').show();

        $.ajax({
            url: 'http://127.0.0.1:8000/order/add',
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                alert("Đã thêm đơn hàng");
                var inputElement = document.getElementById("pageOrder");
                inputElement.value = 0
                $('#uploadProcess').hide();
            },
            error: function(xhr, status, error) {
                alert("Error: " + error);
                $('#uploadProcess').hide();
            }
        });
    }
});
