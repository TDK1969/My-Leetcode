package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	resp, err := http.Get("https://ifconfig.me/ip")
	if err != nil {
		fmt.Println("无法获取公网 IP:", err)
		return
	}
	defer resp.Body.Close()

	ip, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("无法读取响应:", err)
		return
	}

	fmt.Println("公网 IP 地址:", string(ip))
}
