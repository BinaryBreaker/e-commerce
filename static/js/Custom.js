var LiDashboard = document.getElementById("LiDashboard");
var LiAddProduct = document.getElementById("LiAddProduct");
var AllProducts = document.getElementById("LiProduct");
var LiAddCategory = document.getElementById("LiAddCategory");
var LiOrders = document.getElementById("LiOrders");
var LiDashboard2 = document.getElementById("LiDashboard2");
var LiAddProduct2 = document.getElementById("LiAddProduct2");
var LiAddCategory2 = document.getElementById("LiAddCategory2");
var LiOrders2 = document.getElementById("LiOrders2");


function ChangeActive(id) {
    var ActiveSpan = document.getElementById("ActiveSpan");
    var NewSelected = document.getElementById(id);
    var CurrentSelected = ActiveSpan.parentElement;
    var SpanHtml = ActiveSpan.outerHTML;
    ActiveSpan.remove();
    var ATAG = CurrentSelected.children[0];
    var NewSelectedAtag = NewSelected.children[0];
    ATAG.classList.remove("text-gray-800");
    ATAG.classList.remove("dark:text-gray-100");
    NewSelectedAtag.classList.add("dark:text-gray-100");
    NewSelectedAtag.classList.add("text-gray-800");
    NewSelected.insertAdjacentHTML('beforeend', SpanHtml);

}



LiDashboard.onclick = function () {

    ChangeActive("LiDashboard");
    $("#mainContianer").load("/DasBoard").show("slow");

};

LiAddProduct.onclick = function () {
    ChangeActive("LiAddProduct");
    $("#mainContianer").empty();
    $("#mainContianer").hide().load("/AddProduct").show("slow");

};
LiAddCategory.onclick = function () {

    ChangeActive("LiAddCategory");
    $("#mainContianer").empty();
    $("#mainContianer").hide().load("/AddCategory").show("slow");
};
LiOrders.onclick = function () {

    ChangeActive("LiOrders");
    $("#mainContianer").empty();
    $("#mainContianer").hide().load("/Orders").show("slow");
};
AllProducts.onclick = function () {

    ChangeActive("LiProduct");
    $("#mainContianer").empty();
    $("#mainContianer").hide().load("/AllProducts").show("slow");
};

ChangeActive("LiProduct");
$("#mainContianer").empty();
$("#mainContianer").hide().load("/AllProducts").show("slow");

var inp = document.getElementById('searchinput');

inp.addEventListener("input", function (e) {
    var data = $('#searchinput').val()
    data  =  data.replace("'", "\'");
    if (data.length > 2) {
        $('#sugestions').show();
        $.ajax({
            type: 'GET',
            url: "Search/" + data,
            dataType: "json",
            contentType: 'application/json',
            success: function (response) {
                $('#sugestions').empty();
                for (var i = 0; i < response.data.length; i++) {
                    $('#sugestions').append('<p class="mt-2  text-sm text-gray-600 dark:text-gray-400">' + response.data[i] + '</p>');
                    $('#sugestions').append('<hr style="  border-top: 1px solid rgb(226, 226, 226);" class="mt-1 ">');
                }
            }
        });
    } else {
        $('#sugestions').hide();
    }

});