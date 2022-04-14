package com.alex.cnetwork;

import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.util.Enumeration;
import java.util.Objects;

public class qmap {

    private static InetAddress getLocalInetAddress() {
        InetAddress ip = null;
        try {
            Enumeration<NetworkInterface> en_netInterface = NetworkInterface.getNetworkInterfaces();
            while (en_netInterface.hasMoreElements()) {// 是否还有元素
                NetworkInterface ni = (NetworkInterface) en_netInterface.nextElement();// 得到下一个元素
                Enumeration<InetAddress> en_ip = ni.getInetAddresses();// 得到一个ip地址的列举
                while (en_ip.hasMoreElements()) {
                    ip = en_ip.nextElement();
                    if (!ip.isLoopbackAddress() && !Objects.requireNonNull(ip.getHostAddress()).contains(":")) {break;}
                    else {ip = null;}
                }
                if (ip != null) {break;}
            }
        } catch (SocketException e) {e.printStackTrace();}
        return ip;
    }

    public static String c(){
        return "ACSetting";
    }
    public static String a() {
        return "Login";
    }
    public static String protocol() {
        return "http:";
    }
    public static String hostname() {
        return "192.168.7.221";
    }
    public static String iTermType() {
        return "2";
    }
    public static String wlanuserip() {return getLocalInetAddress().toString().replace("/","");}
    public static String wlanacip() {
        return "192.168.130.254";
    }
    public static String wlanacname() {
        return "ME60-X8-1";
    }
    public static String mac() {
        return "c3-eb-01-10-b8-f8";
    }
    public static String ip() {return getLocalInetAddress().toString().replace("/","");}
    public static String enAdvert() {
        return "0";
    }
    public static String queryACIP() {
        return "0";
    }
    public static String loginMethod() {
        return "1";
    }
}
