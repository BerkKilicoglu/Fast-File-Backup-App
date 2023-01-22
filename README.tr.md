
## Fast File Backup App

[![Build Status](https://img.shields.io/badge/lang-T%C3%BCrk%C3%A7e-red)](https://github.com/BerkKilicoglu/Fast-File-Backup-App/blob/main/README.tr.md) [![Build Status](https://img.shields.io/badge/lang-English-blue)](https://github.com/BerkKilicoglu/Fast-File-Backup-App/blob/main/README.md)

![FileBackup Gif1](https://media.giphy.com/media/D010h0DYlZJpcjHalt/giphy.gif)
![FileBackup Gif2](https://media.giphy.com/media/4XsVoileeQMtUakEhL/giphy.gif)

Dosyalarınızı yedeklemek için masaüstü uygulamasıdır. Uygulama, dosyalarınızı hızlıca yedeklemek, yedeklediğiniz dosyaları kolayca takip etmek ve hızlıca geri kurtarmanızı sağlar.


## Özellikler
- **Yerel bilgisayarda** ve **Google Drive** üzerinde dosyalara yedekleme yapılabilir.

- Tüm yedeklemelerinizi **dashboard(gösterge paneli)** bölümünde detaylarıyla görüntüleyebilir ve dosyalarınızı hızlıca kurtabilirsiniz.

- Otomatik yedekleme özelliğiyle zaman periyodu ayarlayıp, o periyotta dosyaları otomatik olarak yedekletebilirsiniz.

- Spesifik dosyaları veya dosya türlerini yedeklemeden hariç tutabilirsiniz.

- Üzerinde değişiklik yapılmayan, zaten mevcut olan dosyalar tekrar yedeklenmez. Bu kontrolü hash(MD5) ile yapar. [performansı iyileştirmek için.]

- Yedeklenen bir klasör için yeni yedekleme noktaları oluşturabilir ve farklı versiyonlarının yedeklerini aynı anda tutabilirsiniz.

## Gereksinimler

**OS**: Windows, Linux or MacOS

**Google Drive API**
> Geliştiriciyseniz ve bu uygulamanın google drive özelliğini kullanıcılarınıza kullandırtmak istiyorsanız cloud.google.com adresinden geliştirici hesabı oluşturup, Google API hizmeti için yeni bir credentials (credentials.json) oluşturmalısınız.
 - **pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib** ile ihtiyaç duyulan tüm kütüphaneleri kurabilirsiniz.

## Yazarlar

 - [BerkKilicoglu](https://github.com/BerkKilicoglu)
 - [emrecpp](https://github.com/emrecpp)