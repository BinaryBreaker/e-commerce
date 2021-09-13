$("#AddButton").click(function () {
    var imgPreview = document.getElementById('img_preview')
    if ($("#fromscat").is(":hidden")){
        $("#New").show();
        $("#Update").hide();
        document.getElementById("fromscat").reset();
        $("#fromscat").show("slow");
        imgPreview.innerHTML = "";
    }
    else{
        $("#fromscat").hide("slow");
        $("#New").hide();
    }
});

var idCurrent = "";


function UpdateForm(){
    var flag =  true;
    if ($("#category").val().length == 0) {
        $("#titlespan").show();
        flag =  false;
    } else
        $("#titlespan").hide();
    if(flag){
        var frm = $('#fromscat')[0];
        var formData = new FormData(frm);
        formData.append('Record',"Other");
        formData.append('id',idCurrent);

        $.ajax({
            type: 'POST',
            url: '/AddCategory/',
            data: formData,
            processData: false,
            contentType: false,
            success: function () {
                $("#mainContianer").empty();
                $("#mainContianer").load("/AddCategory").show("slow");

            }
          });
    }

}
var imgUpload = document.getElementById('upload_imgs')
    , imgPreview = document.getElementById('img_preview')
    ;
imgUpload.addEventListener('change', previewImgs, false);
function previewImgs(event) {
    imgPreview.innerHTML = ""
    imgPreview.classList.remove('quote-imgs-thumbs--hidden');
    previewTitle = document.createElement('p');
    previewTitle.style.fontWeight = 'bold';
    imgPreview.appendChild(previewTitle);
    img = document.createElement('img');
    img.src = URL.createObjectURL(event.target.files[0]);
    img.classList.add('img-preview-thumb');
    imgPreview.appendChild(img);

}

function changeActivecat(id){
    var frm = $('#fromscat')[0];
    var formData = new FormData(frm);
    formData.append('Record',"ACTIVE");
    formData.append('id',id);
    $.ajax({
        
        type: 'post',
        url: '/AddCategory/',
        data: formData,
        processData: false,
        contentType: false,
        success: function () {
            $("#mainContianer").empty();
            $("#mainContianer").load("/AddCategory").show("slow");

        }
      });
}
function EditCat(id){
    $.ajax({
        type: 'GET',
        url: '/api/cat/'+id,
        dataType: "json",
        contentType: 'application/json',
        success: function (response) {
            $("#category").val(response.Name);
            imgPreview.innerHTML = ""
            imgPreview.classList.remove('quote-imgs-thumbs--hidden');
            previewTitle = document.createElement('p');
            previewTitle.style.fontWeight = 'bold';
            imgPreview.appendChild(previewTitle);
            img = document.createElement('img');
            img.src = response.Picture;
            img.classList.add('img-preview-thumb');
            imgPreview.appendChild(img);
            CurrentValueImage =  response.Picture;
            idCurrent = id;
            $("#Update").show();
            $("#New").hide();
            $("#fromscat").show("slow");
        }
      });
}


function SubmitForm() {
    var flag =  true;
    if ($("#category").val().length == 0) {
        $("#titlespan").show();
        flag =  false;
    } else
        $("#titlespan").hide();
    if ($("#upload_imgs").val().length == 0) {
        $("#image").show();
        flag =  false;
    } else
        $("#image").hide();
    if(flag){
        var frm = $('#fromscat')[0];
        var formData = new FormData(frm);
        formData.append('Record',"New");

        $.ajax({
            
            type: 'post',
            url: '/AddCategory/',
            data: formData,
            processData: false,
            contentType: false,
            success: function () {
                $("#mainContianer").empty();
                $("#mainContianer").load("/AddCategory").show("slow");

            }
          });
    }
}