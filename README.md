# Flask Kelime Yönetim Sistemi

Bu proje, kullanıcıların kelimeler ve tanımlarını yönetmesine olanak tanıyan basit bir Flask web uygulamasıdır. Kullanıcılar kayıt olabilir, giriş yapabilir ve kelimeler ekleyip yönetebilirler.

## Özellikler

- Kullanıcı kaydı ve girişi
- Kelime ekleme ve listeleme
- Şifre unutma (placeholder)

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılımlar gereklidir:

- Python 3.6+
- Flask

## Kurulum

1. **Klonlayın:**
    ```bash
    cd flask-kelime-yonetim
    ```

2. **Gerekli Python paketlerini yükleyin:**
    ```bash
    pip install flask
    ```

3. **Proje dizininde gerekli klasörleri oluşturun ve başlangıç dosyalarını hazırlayın:**
    ```bash
    mkdir -p data
    data/words.json
    data/users.json
    ```

## Kullanım

1. **Uygulamayı çalıştırın:**
    ```bash
    python app.py
    ```

2. **Web tarayıcınızda aşağıdaki URL'yi açın:**
    ```
    http://127.0.0.1:5000
    ```

3. **Kullanıcı Kaydı ve Girişi:**
    - Varsayılan kullanıcı adı ve şifre: `ahs` / `ahs`
    - Yeni kullanıcı kaydı yapabilirsiniz.

4. **Kelime Ekleme:**
    - Giriş yaptıktan sonra, kelime ve tanımını ekleyebilirsiniz.

## Dosya Yapısı

- `app.py`: Ana Flask uygulaması
- `templates/`: HTML şablonları
  - `index.html`: Ana sayfa
  - `login.html`: Giriş sayfası
  - `register.html`: Kayıt sayfası
  - `add_word.html`: Kelime ekleme sayfası
  - `forgot_password.html`: Şifre sıfırlama sayfası
- `data/`: JSON veritabanı dosyaları
  - `words.json`: Kelime ve tanımları
  - `users.json`: Kullanıcı bilgileri

## Geliştirme

- Uygulamanın geliştirilmesi için yeni özellikler ekleyebilir, mevcut kodu iyileştirebilir ve hata düzeltmeleri yapılabilir.
- `app.py` ve `templates` dizinindeki dosyaları düzenleyerek uygulamanın işlevselliğini genişletebilirsiniz.

## Lisans

Bu projenin lisansı yoktur. Ücretsiz kullanıma sahiptir.

