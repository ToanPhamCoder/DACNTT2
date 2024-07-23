$(document).ready(function() {
    $('#uploadButtonCategories').click(function() {
        var fileInput = $('#jsonFileCategories')[0];
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
            url: 'http://127.0.0.1:8000/category/add',
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                $('#uploadProcess').hide();
                alert("Đã thêm danh mục");
            },
            error: function(xhr, status, error) {
                $('#uploadProcess').hide();
                alert("Error: " + error);
            }
        });
    }
});
