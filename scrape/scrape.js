var axios = require("axios");
var axiosRetry = require("axios-retry").default;
var fs = require("fs");
let districts=['qalamestan', 'chitgar-lake', 'tehransar', 'azad-shahr', 'sattarkhan', 'gisha', 'khani-abad-no', 'south-janat-abad', 'jamalzadeh', 'bagh-feyz', 'firoozabadi', 'pirouzi', 'shams-abad', 'poonak', 'fallah', 'west-tehranpars', 'qeytariyeh', 'north-sohrevardi', 'vanak', 'sarsabil', 'chitgar', 'gomrok', 'mobarak-abad-e-beheshti', 'marzdaran', 'shahrak-naft-district5', 'shamshiri', 'ostad-moein', 'sharara', 'niavaran', 'sheykh-al-raeis', 'hor-square', 'azarbaijan', 'shahr-e-ziba', 'shadman', 'aseman', 'atabak', 'khavaran', 'kooy-e-ferdos', 'yousef-abad', 'andisheh', 'narmak', 'doolab', 'ajoodanieh', 'shahid-navab-safavi', 'velenjak', 'north-janat-abad', 'jeyhoun', 'aref', 'shiva', 'ekhtiyariyeh', 'tehran-gorgan', 'south-deylaman', 'dr-hoshyar', 'heravi', 'saadat-abad', 'abshar-tehran', 'amiriyeh', 'tehran-zanjan', 'qoba', 'north-shahran', 'darvazeh-shemiran', 'vahidiyeh', 'shokoofeh', 'pasdaran', 'tehran-kerman', 'niroo-havayi', 'nazi-abad', 'south-mehrabad', 'zafaraniyeh', 'amir-bahador', 'azari', 'west-shahrak-e-golestan', 'hakimiyeh', 'sadeghiyeh', 'tehran-lashkar', 'behjat-abad', 'east-shareq', 'heshamatiyeh', 'tarasht', 'south-shahran', 'kamraniyeh', 'darya', 'saeed-abad', 'javadiyeh', 'shirazi', 'bahar', 'parastar', 'mirdamad', 'darrous', 'amir-abad', 'nosrat', 'haftchenar', 'shahrak-e-takhti', 'east-tehranpars', 'sorkhe-hesar', 'khaje-nezam-molk', 'farmaniyeh', 'aghdasieh', 'shahrak-e-vali-e-asr', 'sarsabz', 'abouzar', 'tehran-jolfa', 'beryanak', 'moshiriyeh', 'jey', 'central-janat-abad', 'eslam-abad', 'hesar-booali', 'sazamn-barnameh', 'tehran-hosein-abad', 'soleymani', 'ekbatan', 'salamat', 'shahrak-e-gharb', 'amaniyeh', 'south-narmak', 'evin', 'kooye-e-hefdahom-e-shahrivar', 'tolid-daroo', 'ozgol', 'baqerkhan', 'molavi', 'tayeb', 'mina', 'majid-abad', 'bagh-khazaneh', 'bolursazi', 'elahiyeh', 'mahmoodiyeh', 'aminhozour', 'zafar', 'nezam-abad', 'shabiri', 'tehran-police', 'shahrak-e-parvaz', 'dolat-abad', 'dabestan', 'dolatkhah', 'imamzadeh-hasan', 'aboozar', 'javadiyeh-tehran-pars', 'khalij-e-fars', 'shahrak-e-mahalati', 'jordan', 'shahin', 'jomhouri', 'eshrat-abad', 'yaftabad', 'eskandari', 'emamzade-ghasem', 'hekmat', 'javanmard-e-ghasab', 'shemiran-no', 'shahrak-e-jandarmeri', 'taslihat', 'north-karegar', 'darabad', 'kan', 'nemat-abad', 'afsariyeh', 'moniriyeh', 'valiasr', 'shahrak-e-kianshahr', 'tehran-no', 'minabi', 'shahrak-e-taleghani', 'araj', 'sanglaj', 'saheb-al-zaman', 'sheykh-hadi', 'hashem-abad', 'dezashib', 'ahang', 'fadak', 'charsad-dastgah', 'masoudieh', 'tehranvila', 'gholhak', 'elm-o-sanat', 'qezel-qaleh', 'behdasht', 'vardavard', 'sabalan', 'qasemabad', 'yakhchi-abad', 'aramaneh', 'south-ali-abad', 'zargandeh', 'seyed-khandan', 'dehkade-olympic', 'motahari', 'sizdah-aban', 'imam-sajjad', 'jalili', 'baharan', 'sohanak', 'darakeh', 'sazman-ab', 'shahrak-naft', 'hashemi', 'tohid', 'shaharak-e-shariyati', 'almahdi', 'hasan-abad-shomali', 'tavanir', 'kuy-faraz', 'karevan', 'eram', 'abbas-abad', 'enqelab', 'niloufar', 'golchin', 'zahir-abad', 'qiamdash', 'haft-hoz', 'majidiyeh', 'shahrak-e-vilashahr', 'kuhak']
let arr = [];
async function d(k) {
  await arr.push(k);
}
let n=0
axiosRetry(axios, {
  retries: 3, // number of retries
  retryDelay: (retryCount) => {
    return n * 10000; // time interval between retries
  },
  retryCondition: (error) => {
    // if retry condition is not specified, by default idempotent requests are retried
    n++;
    return true;
  },
});

for (let i = 0; i < 218; i++) {
  axios
    .get(
      "https://api.divar.ir/v8/web-search/tehran/buy-apartment/"+districts[i],

    )
    .then((response) => {
      let data = response.data;
      let tokens = data["server_action_log"]["tokens_info"];
      for (let index = 0; index < tokens.length; index++) {
        let t = tokens[index];
        let token = t["token"];
        if (arr.includes(token)) {
          console.log("block" + token);
          continue;
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
            if (arr.includes(token)) {
              console.log("block" + token);
            } else {
              fs.appendFile(
                "data_raw.csv",
                `${meter},${district},${buildYear},${rooms},${price},${elevator},${space},${parking},${floor}\n`,
                (e) => {
                  if (e) console.log(e);
                  console.log(token);
                  d(token).then(() => {
                    console.log(token);
                  });
                }
              );
            }
          });
      }
    });
}
