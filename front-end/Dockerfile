FROM node:12

# Initialize directory
RUN mkdir /front-end
WORKDIR /front-end
ADD ./ /front-end
COPY . .

# Install depencies
RUN npm install

EXPOSE 3000
