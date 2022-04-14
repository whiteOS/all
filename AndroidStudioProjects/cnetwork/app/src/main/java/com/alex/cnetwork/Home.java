package com.alex.cnetwork;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Map;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.FieldMap;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.POST;
import retrofit2.http.Query;

public class Home extends AppCompatActivity {
    public interface Api {
        @FormUrlEncoded
        @POST("eportal/")
        Call<ResponseBody> getPostDataBody(
                @Query("c") String c, @Query("a") String a, @Query("protocol") String protocol,
                @Query("hostname") String hostname, @Query("iTermType") String iTermType,
                @Query("wlanuserip") String wlanuserip, @Query("wlanacip") String wlanacip,
                @Query("wlanacname") String wlanacname, @Query("mac") String mac,
                @Query("ip") String ip, @Query("enAdvert") String enAdvert,
                @Query("queryACIP") String queryACIP, @Query("loginMethod") String loginMethod,
                @FieldMap Map<String,String> beans);
    }

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_home);

            Button btn_lg = findViewById(R.id.login);
            TextView a = findViewById(R.id.logininfo);

            btn_lg.setOnClickListener(V ->{
                Runnable mt = () -> wifi.connect(Home.this, a);
                Thread mt1 = new Thread(mt, "C");
                mt1.start();
            });
        }
    }

