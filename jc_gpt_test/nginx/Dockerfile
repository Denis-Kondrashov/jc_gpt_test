FROM nginx:1.23-alpine

# Удаляем дефолтный конфиг nginx
RUN rm /etc/nginx/conf.d/default.conf

# Копируем наш конфиг
COPY nginx.conf /etc/nginx/conf.d/

# Создаем директорию для статики
RUN mkdir -p /var/www/jc_gpt_test/static

# Устанавливаем права
RUN chown -R nginx:nginx /var/www/jc_gpt_test && chmod -R 755 /var/www/jc_gpt_test