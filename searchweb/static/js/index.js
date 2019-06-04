function JsonPost(url, data, callback){
    $.ajax({
        type: "POST",
        url: url,
        data: data,
        success: function( data ) {
            console.log(data);
            if (callback != null){
                callback(data);
            }
        },
        dataType: 'json'
    });
}

function JsonGet(url, callback){
    $.getJSON(url, callback);
}



$('#id-search').bind('keypress', function(e) {
    if(e.keyCode==13){
        val = $("#id-search").val()
        JsonPost("/", {
            name:val
        },function(data){
            for(i =0 ; i < data.datas.length; i++ ){
                $("div.body").append(data.datas[i])
            }
            $("#id-search").attr({
                type:"text",
                value:"",
                disabled:false
            })
            document.querySelectorAll('pre code').forEach((block) => {
                hljs.highlightBlock(block);
            });

            // $(".text-card-body").mousover(function(){
            //     $(this).removeAttr("overflow");
            //     $(this).removeAttr("text-overflow");
            //     $(this).removeAttr("max-height");
            // })
            
        })
        $("#id-search").attr({
            type:"button",
            value:"Loading...",
            disabled:true
        })
        $("div.body").html('')
    }
});