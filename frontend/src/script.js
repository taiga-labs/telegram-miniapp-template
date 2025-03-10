const HOST = "https://path_to_docker_gateway";
const API_AUTH_PATH = "/template/api/auth";
const API_PING_PATH = "/template/api/ping";
const SOCKET_PATH = "/template/socket.io";
const ERROR = "Something goes wrong";

window.onload = async function () {
  let socket = io.connect(HOST, { path: SOCKET_PATH });
  socket.on("connect", function () {console.log("socket connection open")});
  socket.on("disconnect", function () {console.log("socket connection closed")});

  let tg = window.Telegram.WebApp;

  let initDataURLSP = new URLSearchParams(tg.initData);
  var hash = initDataURLSP.get("hash");
  initDataURLSP.delete("hash");
  initDataURLSP.sort();
  var checkDataString = initDataURLSP.toString().replaceAll("&", "\n");

  try {
    const response = await fetch(HOST + API_AUTH_PATH, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        data_check_string: checkDataString,
        hash: hash,
      }),
    });
    if (response.status !== 200) {
      const error = response.status === 403 ? await response.text() : ERROR;
      throw error;
    }
  } catch (error) {
    window.stop();
    alert(error);
    return;
  }

  tg.expand();
  tg.MainButton.textColor = "#FFFFFF";
  tg.MainButton.color = "#FF00FF";
  tg.MainButton.text = "Ping";
  tg.MainButton.show();

  Telegram.WebApp.onEvent("mainButtonClicked", async function () {
      let pingResponse;
      try {
        pingResponse = await fetch(HOST + API_PING_PATH + '?' + new URLSearchParams({query_id: tg.initDataUnsafe.query_id,}),
        {
          method: "GET",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
        });
        if (pingResponse.status !== 200) {
          throw error;
        }
      } catch (error) {
        startPage.style.display = "block";
        tg.showAlert(error);
        return;
      }
  });
};