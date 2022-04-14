package com.alex.cnetwork;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button btn_lg = findViewById(R.id.login);
        TextView a = findViewById(R.id.account);
        EditText password = findViewById(R.id.password);
        String uuid = IID.getUUID(MainActivity.this).replace("-","");

        a.setText(uuid);
        IID.setPassword(MainActivity.this, password);

        btn_lg.setOnClickListener(V -> {
            String pda = password.getText().toString();
            String pdb = IID.getPassword(uuid);
            IID.rememberPassword(MainActivity.this, pda);

            if (pdb.equals(pda)) {
                Intent intent = new Intent(MainActivity.this, Home.class);
                startActivity(intent);
                MainActivity.this.finish();
                Toast.makeText(MainActivity.this, "登录成功！", Toast.LENGTH_SHORT).show();
            }else{
                Toast.makeText(MainActivity.this, "密码错误！", Toast.LENGTH_SHORT).show();
            }
        });
    }
}