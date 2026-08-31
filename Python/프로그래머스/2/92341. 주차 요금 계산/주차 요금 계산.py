import math

def solution(fees, records):
    answer = []

    # 현재 입차 중인 차량
    in_time = {}

    # 차량별 누적 주차 시간
    total = {}

    # 기본 시간, 기본 요금, 단위 시간, 단위 요금
    base_time, base_fee, unit_time, unit_fee = fees

    # 입출차 기록 처리
    for record in records:
        time, car, status = record.split()

        hour, minute = map(int, time.split(":"))
        minutes = hour * 60 + minute

        if status == "IN":
            in_time[car] = minutes

        else:
            total[car] = total.get(car, 0) + (minutes - in_time[car])
            del in_time[car]

    # 출차 기록이 없는 차량은 23:59 출차 처리
    end_time = 23 * 60 + 59

    for car, start_time in in_time.items():
        total[car] = total.get(car, 0) + (end_time - start_time)

    # 차량 번호가 작은 순서대로 요금 계산
    for car in sorted(total.keys()):
        total_time = total[car]

        if total_time <= base_time:
            fee = base_fee
        else:
            extra_time = total_time - base_time
            fee = base_fee + math.ceil(extra_time / unit_time) * unit_fee

        answer.append(fee)

    return answer