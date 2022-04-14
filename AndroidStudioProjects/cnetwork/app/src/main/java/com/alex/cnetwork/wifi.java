package com.alex.cnetwork;

import android.app.Activity;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;

import java.io.IOException;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class wifi {
//    public static boolean isNetworkConnected(Activity activity) {
//        ConnectivityManager connMgr = (ConnectivityManager) activity.getApplicationContext().getSystemService(Context.CONNECTIVITY_SERVICE);
//        NetworkInfo networkInfo = connMgr.getActiveNetworkInfo();
//        return (networkInfo != null && networkInfo.isConnected());
//    }

    public static void connect(Activity activity, TextView a){
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://192.168.7.221:801/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        Home.Api request = retrofit.create(Home.Api.class);

        while (!a.toString().equals("登录成功")){
            request.getPostDataBody(qmap.c(),qmap.a(),qmap.protocol(),qmap.hostname(),
                    qmap.iTermType(),qmap.wlanuserip(),qmap.wlanacip(),qmap.wlanacname(),
                    qmap.mac(), qmap.ip(),qmap.enAdvert(),qmap.queryACIP(),qmap.loginMethod(),
                    bean.beans()).enqueue(new Callback<ResponseBody>() {
                @Override
                public void onResponse(@NonNull Call<ResponseBody> call, @NonNull Response<ResponseBody> response) {
                    String r = null;
                    try {
                        if (response.body() != null) {r = response.body().string();}
                    } catch (IOException e) {e.printStackTrace();}
                    if (r != null && r.contains("成功")) {a.setText("登录成功");}
                }
                @Override
                public void onFailure(@NonNull Call call, @NonNull Throwable t) {
                    t.printStackTrace();
                    Toast.makeText(activity, t.toString(), Toast.LENGTH_SHORT).show();
                }
            });
            if (a.toString().equals("登录成功")){return;}
        }
    }
}
