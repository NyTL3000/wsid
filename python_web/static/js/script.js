function scrollToBottom() {
    var a = document.getElementById('bottom')
    a.scrollIntoView({ behavior: 'smooth' })
}
$(document).ready(function () {
    $('#editModal').on('show.bs.modal', function (event) {
        let editForm = document.forms['editForm'];
        let button = $(event.relatedTarget);
        let title = button.data('title');
        let price = button.data('price');
        let image = button.data('image');
        let name = button.data('name');
        console.log(name)
        $('#edittitle').val(title);
        $('#editprice').val(price);
        $('#editimage').val(image);
        editForm.action = ` /manager/edit/product/${title}`;
        
    });
    $('#deleteModal').on('show.bs.modal', function (event) {
        let deleteForm = document.forms['deleteForm'];
        let button = $(event.relatedTarget);
        let title = button.data('title');
        let name = button.data('name');
        console.log(title)
        $('#deletetitle').val(title);
        deleteForm.action = ` /manager/delete/products/${title}`;
        
    });
})


