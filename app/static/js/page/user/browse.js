$( document ).ready(function() {
    console.log( "Ready." );

    $.LoadingOverlay("show");

    // data grid
    $.grid_main("grid-main");

    $.LoadingOverlay("hide");
});

/* define the column of the grid  */
browse_column = function() {
    return [
        {
            caption: "#",
            width: 150,
            fixed: true,
            cellTemplate: function (container, info) {
                var $el = $('<div class="row ml-1 mr-1"></div>');
                $('<a class="btn btn-sm btn-dark col-md-6"><i class="fa fa-pen" aria-hidden="true"></i> Edit</a>')
                    .attr('href', '#')
                    .click(function () {
                        window.location = "addedit.html"
                    }
                    )
                    .appendTo($el);
                $('<a class="btn btn-sm btn-danger col-md-6"><i class="fa fa-trash" aria-hidden="true"></i> Delete</a>')
                    .attr('href', '#')
                    .click(function () {
                        Swal.fire({
                        title: 'Do you want to delete the data?',
                        showDenyButton: true,
                        showCancelButton: true,
                        confirmButtonText: 'Delete',
                        denyButtonText: `Don't delete`,
                        }).then((result) => {
                        /* Read more about isConfirmed, isDenied below */
                        if (result.isConfirmed) {
                            Swal.fire('Delete!', '', 'success')
                        } else if (result.isDenied) {
                            Swal.fire('Data are not deleted', '', 'info')
                        }
                        })
                    }
                    )
                    .appendTo($el);

                container.append($el);
            },
        },
        {
            dataField: 'Name',
        },
        {
            dataField: 'Surname',
        },,
        {
            dataField: 'PhoneNumber',
        },,
        {
            dataField: 'Email',
        },
        {
            dataField: 'SecretCode',
        },
        {
            dataField: 'Status',
            cellTemplate: function (container, options) {
                if (options.value == "TIDAK AKTIF") {
                    $('<h6><span class="badge badge-danger col-12">Inactive</span></h6>').appendTo(container);
                }
                else if (options.value == "AKTIF") {
                    $('<h6><span class="badge badge-success col-12">Active</span></h6>').appendTo(container);
                }
            },
        }
    ];
}

/* create the grid and connect the data */
$.grid_main = function(panel) {
    $('#' + panel).dxDataGrid({
        dataSource: data,
        keyExpr: 'ID',
        selection: {
            mode: 'single',
        },
        hoverStateEnabled: true,
        grouping: {
            autoExpandAll: true,
        },
        groupPanel: {
            visible: true,
        },        
        columnAutoWidth: true,
        columns: browse_column(),
        showBorders: true,
        filterRow: {
            visible: true,
            applyFilter: 'auto',
        },
        searchPanel: {
            visible: true,
            width: 240,
            placeholder: 'Search...',
        },
        headerFilter: {
            visible: true,
        },
        scrolling: {
            rowRenderingMode: 'virtual',
        },
        paging: {
            pageSize: 20,
        },
        pager: {
            visible: true,
            allowedPageSizes: [10, 20, 50, 'all'],
            showPageSizeSelector: true,
            showInfo: true,
            showNavigationButtons: true,
        },
        export: {
            enabled: true,
            allowExportSelectedData: true,
            fileName: "excel-" + uuidv4()
        }
    });
}