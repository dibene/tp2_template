$(document).ready(function(){
    sec = 1000;
    intervalId=0;
    $( "#selectSeconds" ).change(function() {
        sec =  $( "#selectSeconds" ).val();
      });
    $( "#startSamples" ).click(function() {
      sendRequest();
    }); 
    $( "#stopSamples" ).click(function() {
      clearInterval(intervalId);
    });      
      
    function sendRequest(){
        $.ajax({
          url: "/lastten",
          success: 
            function(data){
                average=Array();
                average["temperature"]=0;
                average["humidity"]=0;
                average["pressure"]=0;
                average["windspeed"]=0;

                data.forEach(element => {
                    average["temperature"]+=element.temperature;
                    average["humidity"]+=element.humidity;
                    average["pressure"]+=element.pressure;
                    average["windspeed"]+=element.windspeed; 
                });

                average["temperature"]=average["temperature"]/10;
                average["humidity"]=average["humidity"]/10;
                average["pressure"]=average["pressure"]/10;
                average["windspeed"]=average["windspeed"]/10; 

                $( "#average" ).text(data[0].id+'-'+data[9].id);
                $( "#average_temperature" ).text(average["temperature"]);
                $( "#average_humidity" ).text(average["humidity"]);
                $( "#average_pressure" ).text(average["pressure"]);
                $( "#average_windspeed" ).text(average["windspeed"]);
                $( "#last" ).text(data[0].id);
                $( "#temperature" ).text(data[0].temperature);
                $( "#humidity" ).text(data[0].humidity);
                $( "#pressure" ).text(data[0].pressure);
                $( "#windspeed" ).text(data[0].windspeed);
          },
          complete: function() {
            clearInterval(intervalId);
            intervalId = setInterval(sendRequest, sec); 
       }
      });
    };
  });