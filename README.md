EBS 온라인 클래스 API
======================

처음 작성해보는 API 정리 리포지토리입니다. PR 또는 Issue, Discussions 모두 환영합니다.
-------------

## Base URL
> https://(학교 개별 dns).ebsoc.co.kr/lecture/api/v1

## Headers
> Authorization: Bearer (학생 토큰)

`GET /(학급 ID)/lesson/lecture/attend/list/(수업 ID)`
```json
{
  "code":"OK",
  "message":"요청이 성공하였습니다.",
  "data":{
    "list": [
      {
        "lessonSeq": "수업 아이디",
        "parentLessonSeq": "과목 아이디",
        "orgnlLsnSqno": "", // idk.
        "officeEduCode": "", // idk.
        "schoolCode": "학교 코드",
        "classSeq": 0, // idk.
        "lectureSeq": 0, // idk.
        "lessonType": "", // idk.
        "lessonTypeName": "수업 종류",
        "classUrlPath": "",
        "openYn": "해당 수업이 열려있는지의 여부",  // Y 또는 N
        "courseType": "", // idk.
        "courseTypeName": "주제 종류",
        "lessonName": "수업 이름",
        "lessonIntroduce": "수업 설명",
        "establishMemberSeq": 0,
        "closeMemberSeq": null,
        "courseOpenDate": "", // idk.
        "closeDate": "", // 수업 닫힌 일자로 추정
        "closeYn": "해당 수업이 닫혀있는지의 여부", // Y 또는 N
        "imageFileId": null,
        "imageFileUrl": null,
        "courseCopyAgreeYn": "강좌 복사 여부", // Y 또는 N
        "courseCopyAgreeDate": "",
        "schoolYear": "2021",
        "schoolTypeCode": "M", // Middle School의 M 이라고 추정
        "schoolTypeCodeName": "학교 수준 이름", // 중학교 또는 고등학교 등등
        "schoolGradeCode": "학교 학년 코드", // M03 = 중학생 3학년으로 추정
        "schoolGradeCodeName": "학년",
        "semesterCode": "",
        "semesterCodeName": "학기 이름",
        "material": null, // idk.
        "learnBeginDate": "학습 기간 시작 일자",
        "learnEndDate": "학습 기간 종료 일자",
        "lectureType": "", // idk.
        "lectureTypeName": "", // idk.
        "lessonSort": 1, // idk.
        "lectureStatsCode": null, // idk.
        "lectureStatsCodeName":null, // idk.
        "chapterNo": "해당 과목중 챕터 순서",
        "contentsSeq": 0, // idk.
        "contentsTypeCode": "001", // idk.
        "contentsTypeCodeName": "동영상 일반", // 해당 수업의 종류로 추정
        "subjectList": null, // idk.
        "connectUrlPath":null, // idk.
        "videoUrlPath":null, // idk.
        "delYn": "N", // idk.
        "firstRegistIp": "처음 수업 생성 아이피",
        "firstRegistDate": "수업 생성 날짜",
        "firstRegistUserNo": "수업 생성한 유저의 아이디 Integer",
        "lastUpdateIp": "마지막으로 수정한 아이피",
        "lastUpdateDate": "마지막으로 수정한 날짜",
        "lastUpdateUserNo": "수업 마지막으로 수정한 유저의 아이디 Integer",
        "lessonAttendanceSeq": "Integer", // idk
        "rtpgsRt": "진도 학습률 Integer",
        "learningYn": "Integer", // idk
        "lectureLearningSeq": "Integer" // idk
      }
    ]
  }
}
```