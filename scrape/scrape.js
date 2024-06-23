var axios = require("axios");
var axiosRetry = require("axios-retry").default;
var fs = require("fs");

let arr=[]
async function d(k){
  await arr.push(k)
}
axiosRetry(axios, {
  retries: 50, // number of retries
  retryDelay: (retryCount) => {
    return (retryCount) * 2000; // time interval between retries
  },
  retryCondition: (error) => {
    // if retry condition is not specified, by default idempotent requests are retried
    return true;
  },
});

for (let i = 1500; i < 2000; i++) {
  axios
    .post(
      "https://api.divar.ir/v8/web-search/1/apartment-sell",
      JSON.stringify({
        page: i,
        json_schema: {
          category: {
            value: "apartment-sell",
          },
        },
        "last-post-date": Math.floor(Date.now() * 1000),
      })
    )
    .then((response) => {
      let data = response.data;
      let tokens = data["server_action_log"]["tokens_info"];
      for (let index = 0; index < tokens.length; index++) 
       {
        let t=tokens[index]
        let token = t["token"];
        if(arr.includes(token)){
          console.log("block"+token);
          continue
        }
        axios.default
          .get("https://api.divar.ir/v8/posts-v2/web/" + token)
          .then((r) => {
            let result = r.data;
            s = result.sections;
            let l = 0;
            let meter =
              result["sections"][result["sections"].length - 1]["widgets"][0][
                "data"
              ]["items"][0]["value"];
            let district = result["webengage"]["district"];
            let buildYear =
              result["sections"][result["sections"].length - 1]["widgets"][0][
                "data"
              ]["items"][1]["value"];
            let rooms =
              result["sections"][result["sections"].length - 1]["widgets"][0][
                "data"
              ]["items"][2]["value"];
            let price =
              result["sections"][result["sections"].length - 1]["widgets"][1][
                "data"
              ]["value"];
            let floor = null;
            try {
              for (let k = 0; k < 20; k++) {
                floor =
                  result["sections"][result["sections"].length - 1]["widgets"][
                    k
                  ]["data"]["title"];
                if (floor == "طبقه") {
                  floor =
                    result["sections"][result["sections"].length - 1][
                      "widgets"
                    ][k]["data"]["value"];
                  break;
                }
              }
            } catch {}
            let elevator = true,
              space = true,
              parking = true;
            let group = null;
            for (let k = 0; k < 20; k++) {
              try {
                group =
                  result["sections"][result["sections"].length - 1]["widgets"][
                    k
                  ]["widget_type"];
                if (group == "GROUP_FEATURE_ROW") {
                  group =
                    result["sections"][result["sections"].length - 1][
                      "widgets"
                    ][k]["data"]["items"];
                  break;
                }
              } catch {}
            }
            if (group != null) {
              if (group[0]["title"].includes("ندارد")) {
                elevator = false;
              }
              if (group[1]["title"].includes("ندارد")) {
                space = false;
              }
              if (group[2]["title"].includes("ندارد")) parking = false;
            }
            fs.appendFile(
              "data_raw.csv",
              `${token},${meter},${district},${buildYear},${rooms},${price},${elevator},${space},${parking},${floor}\n`,
              (e) => {
                if (e) console.log(e);
                console.log(token);
                d(token).then(()=>{console.log(token)})
              }
            );

          });
      };
    })
    
}
