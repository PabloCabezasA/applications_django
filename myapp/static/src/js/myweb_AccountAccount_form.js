$(document).ready(function() {

        console.log('el documento está preparado');
        var $form_account =  $('#form_accountAccount').find('input')                
        $form_account.addClass('account_input');
        $form_account.attr('readonly',true);        
        $("#button_guardar").hide();
        $("#button_edit_tree").hide();

        
//funcion del boton editar para dejar campos editables
        $('#button_edit').click(function () {
    	$form_account.attr('readonly',false);
    	$("#button_guardar").show();
		});


//funcion ejecuta el formulario al clickear para editar        
        $('.check_table').click(function() {
        var $check = $('.check_table').is(':checked');        
        if ($check) {
            $('#button_edit_tree').show()
        	}
        else{
        	$('#button_edit_tree').hide();
        }
        var $check = $('input:checkbox:checked.check_table').map(function () {
  					return this.value;
					}).get();
        console.log($check)
    	});

});