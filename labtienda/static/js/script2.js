$(document).ready(function() {
    $('#clientes').DataTable({

        responsive: 'True',
        dom: 'Bfrtip',
        buttons: [{
                extend: 'copyHtml5',
                text: '<i class="fa fa-files-o fa-2x"></i>',
                titleAttr: 'Copy',
                className: 'btn btn-secondary'
            },
            {
                extend: 'excelHtml5',
                text: '<i class="fa fa-file-excel-o fa-2x"></i>',
                titleAttr: 'Excel',
                className: 'btn btn-success'
            },
            {
                extend: 'csvHtml5',
                text: '<i class="fa fa-file-text-o fa-2x"></i>',
                titleAttr: 'CSV',
                className: 'btn btn-dark'
            },
            {
                extend: 'pdfHtml5',
                text: '<i class="fa fa-file-pdf-o fa-2x"></i>',
                titleAttr: 'PDF',
                className: 'btn btn-danger'
            },
            {
                extend: 'print',
                text: '<i class="fa fa-print fa-2x" aria-hidden="true"></i>',
                titleAttr: 'Print',
                className: 'btn btn-info'
            },

        ],
        language: {
            "decimal": "",
            "emptyTable": "No hay datos",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
            "infoEmpty": "Mostrando 0 a 0 de 0 registros",
            "infoFiltered": "(Filtro de _MAX_ total registros)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Ver _MENU_ registros",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "No se encontraron coincidencias",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Ultimo",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "aria": {
                "sortAscending": ": Activar orden de columna ascendente",
                "sortDescending": ": Activar orden de columna desendente"
            }
        }
    });
});