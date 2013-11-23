function dish_crud(dish_id,dish_name,dish_price){
  if(!meal_id_list.hasObject(dish_id)){
    meal_id_list.push(dish_id);
    $("#dish_"+dish_id).html("remove");
    $("#order_table").append("<tr id='tr_"+dish_id+"'><td>"+dish_name+"</td><td>"+dish_price+"</td></tr>");
    $("#show_order").show();
    var has_cost = $("#total_cost").html() == ''?0:parseInt($("#total_cost").html());
    var cost = has_cost+dish_price;
    $("#total_cost").html(cost);
    $("#submit_div").show();


  }
  else{
    meal_id_list.splice(meal_id_list.indexOf(dish_id),1);
    $("#total_cost").html(parseInt($("#total_cost").html())-dish_price);
    $("#tr_"+dish_id).remove();
    $("#dish_"+dish_id).html("add");
    if(meal_id_list.length <= 0){
      $("#show_order").hide();
      $("#submit_div").hide();
    }
  }
}

function submit_bill(){
	var select_meal = ""
	for(var i = 0;i<meal_id_list.length;i++){
		if(select_meal !=''){
			select_meal += "&";
		}
		select_meal +='meal_id='+meal_id_list[i];
		
	}
	select_meal+="&cost="+parseInt($("#total_cost").html());
	$.ajax({
		url:"order",
		type:"post",
		data:select_meal,
		success:function(data){
			location.href = "user";
		},
	})
}