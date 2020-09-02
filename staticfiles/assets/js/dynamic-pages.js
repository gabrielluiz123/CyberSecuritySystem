
var onRequest = false;
var data = {
    sections: Array,
    sectionEditing: false,
    currSectionTitle: "",
    subsectionTitleEditing: false,
    currSubsectionTitle: "",
    subsectionContentEditing: false,
    currSubsectionContent: "",
    currDeleting: "",
    currSubsectionDeleting: "",
    isAuth: Boolean,
    ref: "0"
}
var page = new Vue({
    el: "#dynamic-page",
    data: data,
    methods: {
        getSections: function () {
            $.post('/api/pages', {
                exec: 'get_sections',
                routeName: window.location.pathname.substr(1)
            }, null, 'json').then(function (r) {
                data.sections = r;
            });
        },
        tinyMCE: function (action) {
            var id = 'txa_' + data.subsectionContentEditing;
            if (action == 'start') {
                for (var i = tinymce.editors.length - 1 ; i > -1 ; i--) {
                    var ed_id = tinymce.editors[i].remove();
                }
                setTimeout(function () {
                    tinymce.init({
                        selector: '#' + id,
                        height: 200,
                        plugins: ['media', 'image', 'code', 'fontawesome noneditable'],
                        image_caption: true,
                        content_css: 'https://netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css',
                        noneditable_noneditable_class: 'fa',
                        toolbar: 'fontawesome',
                        extended_valid_elements: 'span[*]',
                        setup: function (e) {
                            e.on('init',
                                function (e) {
                                    tinymce.get(id).setContent(data.currSubsectionContent)
                                }
                            );
                        },
                    });
                }, 200);
            }
            if (action == 'finish') {
                tinyMCE.get(id).remove();
                data.subsectionContentEditing = false
            }
        },
        printData: function () {
            console.log(this.isAuth);
        },
        changeSectionTitle: function (idx) {
            $.post('/api/pages', {
                exec: 'update_section_name',
                id: data.sectionEditing,
                title: data.currSectionTitle
            }, null, 'json').then(function (r) {
                if ('erro' in r) {
                    simpleAlert.show({
                        message: 'Algo deu errado ao atualizar..',
                    });
                } else {
                    simpleAlert.show({
                        message: 'Título atualizado com sucesso!',
                        type: 'success'
                    })
                }
            });
            data.sections[idx].name = data.currSectionTitle;
            data.currSectionTitle = "";
            data.sectionEditing = false;
        },
        changeSubsectionTitle: function (idx, ids) {
            $.post('/api/pages', {
                exec: 'update_subsection_title',
                id: data.subsectionTitleEditing,
                title: data.currSubsectionTitle
            }, null, 'json').then(function (r) {
                if ('erro' in r) {
                    simpleAlert.show({
                        message: 'Algo deu errado ao atualizar..',
                    });
                } else {
                    simpleAlert.show({
                        message: 'Título da subseção atualizado com sucesso!',
                        type: 'success'
                    })
                }
            });
            data.sections[idx].subsections[ids].title = data.currSubsectionTitle;
            data.currSubsectionTitle = "";
            data.subsectionTitleEditing = false;
        },
        changeSubsectionContent: function (idx, ids) {
            if (onRequest) return false;
            onRequest = true;
            data.currSubsectionContent = tinyMCE.get('txa_' + data.subsectionContentEditing).getContent();
            $.post('/api/pages', {
                exec: 'update_subsection_content',
                id: data.subsectionContentEditing,
                content: data.currSubsectionContent
            }, null, 'json').then(function (r) {
                if ('erro' in r) {
                    simpleAlert.show({
                        message: 'Algo deu errado ao atualizar..',
                    });
                } else {
                    simpleAlert.show({
                        message: 'Conteúdo da seção atualizado com sucesso!',
                        type: 'success'
                    })
                }
                onRequest = false;
            });
            page.tinyMCE('finish');
            data.sections[idx].subsections[ids].content = data.currSubsectionContent;
            data.currSubsectionContent = "";
            data.subsectionContentEditing = false;

        },
        addSection: function () {
            if (onRequest) return false;
            onRequest = true;
            var d = new Date();
            var section = {
                sectionName: "Nova Seção",
                name: "Nova Seção",
                subsections: [{
                    ssTitle: "Título da Subseção",
                    ssContent: "Conteúdo da subseção",
                    title: "Título da Subseção",
                    content: "Conteúdo da subseção",
                    id: d.getTime()
                }],
                id: d.getTime(),
                ref: data.ref
            };
            $.post('/api/pages', {
                exec: 'add_new_section',
                data: section
            }, null, 'json').then(function (r) {
                page.getSections();
                if ('erro' in r) {
                    simpleAlert.show({
                        message: 'Houve um problema ao adicionar a seção..'
                    })
                }
                onRequest = false;
            });
        },
        deleteSection(idx, confirm = false) {
            data.currDeleting = idx;
            $('#confirm_modal').modal('show');
            if (confirm == true) {
                $.post('/api/pages', {
                    exec: 'remove_section',
                    ref: data.sections[idx].id
                }, null, 'json').then(function (r) {
                    if ('erro' in r) {
                        simpleAlert.show({
                            message: "Houve um porblema ao excluir a seção. Por favor, tente novamente.",
                        });
                    } else {
                        data.sections.splice(idx, 1);
                        data.currDeleting = "";
                        simpleAlert.show({
                            message: "Seção excluída com sucesso!",
                            type: 'success'
                        });
                    }

                })
                $('#confirm_modal').modal('hide');
            }
        },
        deleteSubsection: function (idx, ids, confirm = false) {
            data.currDeleting = idx;
            data.currSubsectionDeleting = ids;
            $('#confirm_subsection_modal').modal('show');
            if (confirm == true) {
                $.post('/api/pages', {
                    exec: 'remove_subsection',
                    ref: data.sections[idx].subsections[ids].id
                }, null, 'json').then(function (r) {
                    if ('erro' in r) {
                        simpleAlert.show({
                            message: "Houve um porblema ao excluir esta subseção. Por favor, tente novamente.",
                        });
                    } else {
                        data.sections[idx].subsections.splice(ids, 1);
                        data.currDeleting = "";
                        simpleAlert.show({
                            message: "Subseção excluída com sucesso!",
                            type: 'success'
                        });
                    }
                });
                $('#confirm_subsection_modal').modal('hide');
            }
        },
        addSubsection: function (idx) {
            if (onRequest) return false;
            onRequest = true;
            var d = new Date();
            var subsection = {
                    ssTitle: "Título da Subseção",
                    ssContent: "Conteúdo da subseção",
                    id: d.getTime(),
                    ref: data.sections[idx].id
                };
            $.post('/api/pages', {
                exec: 'add_new_subsection',
                data: subsection
            }, null, 'json').then(function (r) {
                page.getSections();
                if ('erro' in r) {
                    simpleAlert.show({
                        message: 'Houve um problema ao adicionar a seção..'
                    })
                }
                onRequest = false;
            });
        },
        swapSections: function(idx)
        {
            if(data.onRequest) return false;

            data.onRequest = true;
            $.post('/api/pages', {
                exec: 'swap_sections_position',
                sections: [
                    {
                        id: data.sections[idx].id,
                        position: idx-1,
                    },
                    {
                        id: data.sections[idx-1].id,
                        position: idx
                    }
                ]    
            }, null, 'json').then(function(r){

                if('erro' in r){
                    simpleAlert.show({
                        message: 'Houve um problema ao executar esta ação..'
                    });
                }else{
                    data.sections[idx].position--;           
                    data.sections[idx-1].position++;           
                    data.sections.splice(idx-1, 2, data.sections[idx], data.sections[idx-1]);
                }
                data.onRequest = false;
            });
        }
    },

    created: function () {
        this.getSections();
    }
});


var head = {
    header: Array,
    currHeaderTitle: "",
    currHeaderSubtitle: "",
    editingHeaderTitle: false,
    editingHeaderSubtitle: false,
    isAuth: Boolean
}

var header = new Vue({
    el: '#main-header',
    data: head,
    methods: {
        getPage: function () {
            $.post('/api/pages', {
                exec: 'get_page',
                route: window.location.pathname.substr(1)
            }, null, 'json').then(function (r) {
                head.header = r[0];
                data.ref = r[0].id;
            });
        },
        changeHeaderTitle: function () {
            $.post('/api/pages', {
                exec: 'update_header_title',
                id: head.header.id,
                title: head.currHeaderTitle
            }, null, 'json').then(function (r) {
                if ('erro' in r) {
                    simpleAlert.show({
                        message: 'Algo deu errado ao atualizar..',
                    });
                } else {
                    simpleAlert.show({
                        message: 'Título da página atualizado com sucesso!',
                        type: 'success'
                    })
                }
            });
            head.header.title = head.currHeaderTitle;
            head.currHeaderTitle = "";
            head.editingHeaderTitle = false;
        },
        changeHeaderSubtitle: function () {
            $.post('/api/pages', {
                exec: 'update_header_subtitle',
                id: head.header.id,
                subtitle: head.currHeaderSubtitle
            }, null, 'json').then(function (r) {
                if ('erro' in r) {
                    simpleAlert.show({
                        message: 'Algo deu errado ao atualizar..',
                    });
                } else {
                    simpleAlert.show({
                        message: 'Subtítulo da página atualizado com sucesso!',
                        type: 'success'
                    })
                }
            });
            head.header.subtitle = head.currHeaderSubtitle;
            head.currHeaderSubtitle = "";
            head.editingHeaderSubtitle = false;
        },

        printData: function () {
            console.log(head.header);

        }

    },
    created: function () {
        this.getPage();
        setInterval(function () {
            if (data.isAuth !== auth) {
                data.isAuth = auth;
                head.isAuth = auth;
            }
        }, 100)
    }
})

function getResponse(r) {
    return r;
}