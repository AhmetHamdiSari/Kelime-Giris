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

1. **Depoyu klonlayın:**
    ```bash
    git clone https://github.com/kullanici/flask-kelime-yonetim.git
    cd flask-kelime-yonetim
    ```

2. **Gerekli Python paketlerini yükleyin:**
    ```bash
    pip install flask
    ```

3. **Proje dizininde gerekli klasörleri oluşturun ve başlangıç dosyalarını hazırlayın:**
    ```bash
    mkdir -p data
    echo "[]" > data/words.json
    echo "[]" > data/users.json
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

- `app.py`: Ana Flask uygulaması.
- `templates/`: HTML şablonları.
  - `index.html`: Ana sayfa şablonu.
  - `login.html`: Giriş sayfası şablonu.
  - `register.html`: Kayıt sayfası şablonu.
  - `add_word.html`: Kelime ekleme sayfası şablonu.
  - `forgot_password.html`: Şifre sıfırlama sayfası şablonu.
- `data/`: JSON veritabanı dosyalarını içerir.
  - `words.json`: Kelime ve tanımları saklar.
  - `users.json`: Kullanıcı bilgilerini saklar.

## Geliştirme

- Uygulamanın geliştirilmesi için yeni özellikler ekleyebilir, mevcut kodu iyileştirebilir ve hata düzeltmeleri yapabilirsiniz.
- `app.py` ve `templates` dizinindeki dosyaları düzenleyerek uygulamanın işlevselliğini genişletebilirsiniz.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

