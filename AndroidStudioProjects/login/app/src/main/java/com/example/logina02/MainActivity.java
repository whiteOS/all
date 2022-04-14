package com.example.logina02;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.alibaba.fastjson.JSONObject;
import com.google.gson.Gson;

import java.io.IOException;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.Body;
import retrofit2.http.POST;

public class MainActivity extends AppCompatActivity {

    public interface Api {
        @POST("login/")
        Call<ResponseBody> getPostDataBody(@Body JSONObject body);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        EditText ac = findViewById(R.id.account);
        EditText pd = findViewById(R.id.password);
        Button btn_lg = findViewById(R.id.login);

        btn_lg.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View V){
                String a = ac.getText().toString();
                String p = pd.getText().toString();
                Retrofit retrofit = new Retrofit.Builder()
                        .baseUrl("http://10.64.70.123:5000/") // 设置网络请求baseUrl
                        .addConverterFactory(GsonConverterFactory.create(new Gson())) //设置使用Gson解析
                        .build();
                Api request = retrofit.create(Api.class);
                JSONObject json = new JSONObject();
                json.put("id", a);
                json.put("pd", p);
                request.getPostDataBody(json).enqueue(new Callback<ResponseBody>() {
                    @Override
                    public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                        try {
                            String r = response.body().string();
                            Toast.makeText(MainActivity.this, r, Toast.LENGTH_SHORT).show();
                            if (r.equals("Welcome!")){
                                Intent intent = new Intent(MainActivity.this, Home.class);
                                startActivity(intent);
                                MainActivity.this.finish();
                            }
                        } catch (IOException e) {
                            e.printStackTrace();
                            Toast.makeText(MainActivity.this, e.toString(), Toast.LENGTH_SHORT).show();
                        }
                    }

                    @Override
                    public void onFailure(Call<ResponseBody> call, Throwable t) {
                        Toast.makeText(MainActivity.this, t.toString(), Toast.LENGTH_SHORT).show();
                    }
                });
                }
        });
    }
}
