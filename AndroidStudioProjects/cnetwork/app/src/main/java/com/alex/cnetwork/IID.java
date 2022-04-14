package com.alex.cnetwork;

import android.content.Context;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.widget.EditText;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.Calendar;
import java.util.Random;
import java.util.UUID;

public class IID {
        private static String sID = null;
        private static final String INSTALLATION = "INSTALLATION";
        public synchronized static String getUUID(Context context) {
            if (sID == null) {
                File installation = new File(context.getFilesDir(), INSTALLATION);
                try {
                    if (!installation.exists())
                        writeInstallationFile(installation);
                    sID = readInstallationFile(installation);
                } catch (Exception e) {
                    throw new RuntimeException(e);
                }
            }
            return sID;
        }
        private static String readInstallationFile(File installation) throws IOException {
            RandomAccessFile f = new RandomAccessFile(installation, "r");
            byte[] bytes = new byte[(int) f.length()];
            f.readFully(bytes);
            f.close();
            return new String(bytes);
        }
        private static void writeInstallationFile(File installation) throws IOException {
            FileOutputStream out = new FileOutputStream(installation);
            String id = UUID.randomUUID().toString();
            out.write(id.getBytes());
            out.close();
        }

        public static String getPassword(String uuid){
            Calendar mo = Calendar.getInstance();
            Random random = new Random(mo.get(Calendar.MONTH) + 100);
            StringBuilder pd = new StringBuilder();
            for(int i=0;i<32;i++){
                int number=random.nextInt(32);
                pd.append(uuid.charAt(number));
            }
            return pd.toString();
        }

        public static void setPassword(Context context, EditText password){
            SharedPreferences pref;
            pref = PreferenceManager.getDefaultSharedPreferences(context);
            password.setText(pref.getString("password",""));
        }

        public static void rememberPassword(Context context, String password){
            SharedPreferences pref;
            SharedPreferences.Editor editor;
            pref = PreferenceManager.getDefaultSharedPreferences(context);
            editor = pref.edit();
            editor.putString("password", password);
            editor.apply();
        }
}
