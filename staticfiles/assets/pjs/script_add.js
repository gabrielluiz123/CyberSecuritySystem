function aprovar_line_equip(i)
{
    if(document.getElementById("aprovado_equip"+i).value == 1)
    {
        document.getElementById('btnAprovar_line_equip'+i).classList.remove("btn-success");
        document.getElementById('btnAprovar_line_equip'+i).classList.add("btn-danger");
        document.getElementById('btnAprovar_line_equip'+i).innerHTML = "Reprovado";
        document.getElementById('aprovado_equip'+i).value = 0;
    }
    else
    {
        document.getElementById('btnAprovar_line_equip'+i).classList.remove("btn-danger");
        document.getElementById('btnAprovar_line_equip'+i).classList.add("btn-success");
        document.getElementById('btnAprovar_line_equip'+i).innerHTML = "Aprovado";
        document.getElementById('aprovado_equip'+i).value = 1;
    }

}

function aprovar_line_acess(i)
{
    console.log(i);
    if(document.getElementById("aprovado_acess"+i).value == 1)
    {
        document.getElementById('btnAprovar_line_acess'+i).classList.remove("btn-success");
        document.getElementById('btnAprovar_line_acess'+i).classList.add("btn-danger");
        document.getElementById('btnAprovar_line_acess'+i).innerHTML = "Reprovado";
        document.getElementById('aprovado_acess'+i).value = 0;
    }
    else
    {
        document.getElementById('btnAprovar_line_acess'+i).classList.remove("btn-danger");
        document.getElementById('btnAprovar_line_acess'+i).classList.add("btn-success");
        document.getElementById('btnAprovar_line_acess'+i).innerHTML = "Aprovado";
        document.getElementById('aprovado_acess'+i).value = 1;
    }

}

function clickClienteL()
{
     document.getElementById('nav-home-tab').classList.remove("active");
     document.getElementById('nav-contact-tab1').classList.add("active");
     document.getElementById('nav-contact-tab').classList.remove("active");
     var elmnt = document.getElementById("contact");
     elmnt.scrollIntoView();
}

function clickClienteR()
{

     document.getElementById('nav-home-tab').classList.remove("active");
     document.getElementById('nav-contact-tab1').classList.add("active");
     document.getElementById('nav-contact-tab').classList.remove("active");
     var elmnt = document.getElementById("contact");
     elmnt.scrollIntoView();

}

function clickInfoR()
{
     document.getElementById('nav-home-1').classList.remove("active");
     document.getElementById('nav-home-tab').classList.add("active");
     document.getElementById('nav-contact-tab-1').classList.remove("active");
     var elmnt = document.getElementById("contact");
     elmnt.scrollIntoView();
}

function consultaCNPJRV()
{
    var json = consultaCNPJ2();
    json.then(function(value) {
        if(value.situacao != "ATIVA")
        {
            alert("CNPJ não está com situação ativa!");
        }
        document.getElementById('razao_revenda').value = value.nome;
        document.getElementById('state_revenda').value = value.uf;
        document.getElementById('cep_revenda').value = value.cep;
        document.getElementById('address_revenda').value = value.logradouro;
        document.getElementById('city_revenda').value = value.municipio;
        if(document.getElementById('situacao_revenda'))
        {
            document.getElementById('email_revenda').value = value.situacao;
        }
}, function(value) {
  //
});
}

function consultaCNPJ()
{
    var json = consultaCNPJ2();
    json.then(function(value) {
        if(value.situacao != "ATIVA")
        {
            alert("CNPJ não está com situação ativa!");
        }
        console.log(value)
        document.getElementById('razao_cliente').value = value.nome;
        document.getElementById('state_cliente').value = value.uf;
        document.getElementById('cep_cliente').value = value.cep;
        document.getElementById('address_cliente').value = value.logradouro;
        document.getElementById('city_cliente').value = value.municipio;
}, function(value) {
  //
});
}

function consultaCNPJ2() {
    if(document.getElementById('cnpj_cliente'))
    {
        var cnpj = document.getElementById('cnpj_cliente').value;
    }
    else
    {
        var cnpj = document.getElementById('cnpj_revenda').value;
    }


    cnpj = cnpj.replace(/\D/g, '');

    return jsonp('https://www.receitaws.com.br/v1/cnpj/' + encodeURI(cnpj), 60000)
        .then(function(json)  {
            if (json['status'] === 'ERROR') {
                return Promise.reject(json['message']);
            } else {
                return Promise.resolve(json);
            }
        });
}

function clickC()
{
    document.getElementById('nav-profile-tab1').classList.remove("active");
    document.getElementById('nav-contact-tab1').classList.add("active");
    document.getElementById('nav-contact-tab2').classList.remove("active");
    var elmnt = document.getElementById("contact");
    elmnt.scrollIntoView();
}

function clickEquip()
{
    document.getElementById('nav-concorrente-tab').classList.remove("active");
    document.getElementById('nav-about-vendedor-tab').classList.add("active");
    document.getElementById('nav-about-vendedor-tab1').classList.remove("active");
    var elmnt = document.getElementById("contact");
    elmnt.scrollIntoView();
}

function clickEquipConcorrente()
{
console.log("AQUI");
    document.getElementById('nav-about-tab').classList.remove("active");
    document.getElementById('nav-concorrente-tab').classList.add("active");
    document.getElementById('nav-concorrente').classList.add("active");
    var elmnt = document.getElementById("contact");
    elmnt.scrollIntoView();
}

function clickCliente()
{
    document.getElementById('nav-home-tab').classList.remove("active");
    document.getElementById('nav-profile-tab1').classList.add("active");
    document.getElementById('nav-contact-tab').classList.remove("active");
    var elmnt = document.getElementById("contact");
    elmnt.scrollIntoView();
}

function clickInfo()
{
    document.getElementById('nav-contact-tab1').classList.remove("active");
    document.getElementById('nav-about-tab').classList.add("active");
    document.getElementById('nav-about-tab1').classList.remove("active");
    var elmnt = document.getElementById("contact");
    elmnt.scrollIntoView();
}

function add()
{
    var tb1 = document.createElement("tr");
	document.getElementById("tbpn").appendChild(tb1);
	var row = document.getElementsByTagName('tr');
	var i = 0;
	for(j=0; j<1000; j++)
	{
	    if(document.getElementById('pn_projeto'+j))
	    {
	        i++;
	    }
	    else
	    {
	        j=200000;
	    }
	}
	var length = i;
	console.log(length)
	tb1.innerHTML+= '<td><input type="text" name="pn_projeto'+length+'" id="pn_projeto'+length+'" class="form-control shadow-none my-1"></td>';
	tb1.innerHTML+='<td><input type="text" name="desc_projeto'+length+'" id="desc_projeto'+length+'" class="form-control shadow-none my-1"></td>';
	tb1.innerHTML+='<td><input type="text" name="qty_projeto'+length+'" id="qty_projeto'+length+'" class="form-control shadow-none my-1"></td>';
	tb1.innerHTML+='<td><input type="text" name="value_projeto'+length+'" id="value_projeto'+length+'" class="form-control shadow-none my-1"></td>';
    tb1.innerHTML+='<td><a style="color: white;" id="btn_pn'+length+'" class="btn btn-danger" onclick="rm_pn('+length+')">X</a></td>';
    tb1.innerHTML+='<td><input style="color: black;" value="1"  type="hidden" name="aprovado_equip'+length+'" id="aprovado_equip'+length+'" class="form-control shadow-none my-1"></td>';
}

function rm_pn(num)
{
    var c1 = document.getElementById("pn_projeto"+num);
    c1.parentNode.removeChild(c1);
    var c2 = document.getElementById("desc_projeto"+num);
    c2.parentNode.removeChild(c2);
    var c3 = document.getElementById("qty_projeto"+num);
    c3.parentNode.removeChild(c3);
    var c4 = document.getElementById("value_projeto"+num);
    c4.parentNode.removeChild(c4);
    var c5 = document.getElementById("btn_pn"+num);
    c5.parentNode.removeChild(c5);
}

function rm_ac(num)
{
    var c1 = document.getElementById("ac_pn_projeto"+num);
    c1.parentNode.removeChild(c1);
    var c2 = document.getElementById("ac_desc_projeto"+num);
    c2.parentNode.removeChild(c2);
    var c3 = document.getElementById("ac_qty_projeto"+num);
    c3.parentNode.removeChild(c3);
    var c4 = document.getElementById("ac_value_projeto"+num);
    c4.parentNode.removeChild(c4);
    var c5 = document.getElementById("ac_btn_pn"+num);
    c5.parentNode.removeChild(c5);
}

function rm_acc(num)
{
    var c1 = document.getElementById("c_pn_projeto"+num);
    c1.parentNode.removeChild(c1);
    var c2 = document.getElementById("c_desc_projeto"+num);
    c2.parentNode.removeChild(c2);
    var c3 = document.getElementById("c_qty_projeto"+num);
    c3.parentNode.removeChild(c3);
    var c4 = document.getElementById("c_value_projeto"+num);
    c4.parentNode.removeChild(c4);
    var c5 = document.getElementById("c_btn_pn"+num);
    c5.parentNode.removeChild(c5);
}

function add_ac()
{
    var tb1 = document.createElement("tr");
	document.getElementById("tbac").appendChild(tb1);
	var row = document.getElementsByTagName('tr');
	var i = 0;
	for(j=0; j<1000; j++)
	{
	    if(document.getElementById('ac_pn_projeto'+j))
	    {
	        i++;
	    }
	    else
	    {
	        j=200000;
	    }
	}
	var length2 = i;
	console.log(length2)
	tb1.innerHTML+= '<td><input type="text" name="ac_pn_projeto'+length2+'" id="ac_pn_projeto'+length2+'" class="form-control shadow-none my-1"></td>';
	tb1.innerHTML+='<td><input type="text" name="ac_desc_projeto'+length2+'" id="ac_desc_projeto'+length2+'" class="form-control shadow-none my-1"></td>';
	tb1.innerHTML+='<td><input type="text" name="ac_qty_projeto'+length2+'" id="ac_qty_projeto'+length2+'" class="form-control shadow-none my-1"></td>';
	tb1.innerHTML+='<td><input type="text" name="ac_value_projeto'+length2+'" id="ac_value_projeto'+length2+'" class="form-control shadow-none my-1"></td>';
	tb1.innerHTML+='<td><a style="color: white;" id="ac_btn_pn'+length2+'" class="btn btn-danger" onclick="rm_ac('+length2+')">X</a></td>';
    tb1.innerHTML+='<td><input style="color: black;" value="1"  type="hidden" name="aprovado_acess'+length+'" id="aprovado_acess'+length+'" class="form-control shadow-none my-1"></td>';
}

function add_acc()
{
    var tb1 = document.createElement("tr");
	document.getElementById("tbacc").appendChild(tb1);
	var row = document.getElementsByTagName('tr');
	var i =0;
	for(j=0; j<1000; j++)
	{
	    if(document.getElementById('c_pn_projeto'+j))
	    {
	        i++;
	    }
	    else
	    {
	        j=200000;
	    }
	}

	var length2 = i;
	tb1.innerHTML+= '<td><input type="text" name="c_pn_projeto'+length2+'" id="c_pn_projeto'+length2+'" class="form-control shadow-none my-1"></td>';
	tb1.innerHTML+='<td><input type="text" name="c_desc_projeto'+length2+'" id="c_desc_projeto'+length2+'" class="form-control shadow-none my-1"></td>';
	tb1.innerHTML+='<td><input type="text" name="c_qty_projeto'+length2+'" id="c_qty_projeto'+length2+'" class="form-control shadow-none my-1"></td>';
	tb1.innerHTML+='<td><input type="text" name="c_value_projeto'+length2+'" id="c_value_projeto'+length2+'" class="form-control shadow-none my-1"></td>';
	tb1.innerHTML+='<td><a style="color: white;" id="c_btn_pn'+length2+'" class="btn btn-danger" onclick="rm_acc('+length2+')">X</a></td>';
    tb1.innerHTML+='<td><input style="color: black;" value="1"  type="hidden" name="aprovado_acess'+length+'" id="aprovado_acess'+length+'" class="form-control shadow-none my-1"></td>';
}