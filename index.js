const express = require('express');
const app = express();

// 루트 URL에 대한 요청 처리
app.get('/', (req, res) => {
  res.send('안녕하세요! 이것은 Express.js를 사용하여 작성한 웹 서버입니다.');
});

// 서버 실행
app.listen(3000, () => {
  console.log('서버가 실행 중입니다!');
});
