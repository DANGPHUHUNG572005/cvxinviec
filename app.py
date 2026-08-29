import streamlit as st

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="CV - Đặng Phú Hưng",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS - THIẾT KẾ GIAO DIỆN CV
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f3f4f6;
}

/* Ẩn menu Streamlit */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Khung CV chính */
.cv-container {
    max-width: 1100px;
    margin: 30px auto;
    background: white;
    box-shadow: 0 10px 35px rgba(0,0,0,0.10);
    border-radius: 12px;
    overflow: hidden;
}

/* Header */
.cv-header {
    background: linear-gradient(135deg, #17365d, #1f4e79);
    color: white;
    padding: 42px 50px;
}

.cv-name {
    font-size: 38px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.cv-position {
    font-size: 17px;
    font-weight: 500;
    opacity: 0.95;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Thông tin cá nhân */
.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px 30px;
    margin-top: 25px;
}

.contact-item {
    font-size: 14px;
    line-height: 1.6;
}

.contact-label {
    font-weight: 700;
    margin-right: 5px;
}

/* Nội dung */
.cv-body {
    display: grid;
    grid-template-columns: 34% 66%;
}

/* Cột trái */
.left-column {
    background: #f7f9fc;
    padding: 35px 30px;
    border-right: 1px solid #e4e7eb;
}

/* Cột phải */
.right-column {
    padding: 35px 40px;
}

/* Section */
.section {
    margin-bottom: 32px;
}

.section-title {
    color: #17365d;
    font-size: 17px;
    font-weight: 800;
    text-transform: uppercase;
    border-bottom: 2px solid #17365d;
    padding-bottom: 8px;
    margin-bottom: 17px;
    letter-spacing: 0.5px;
}

/* Text */
.text {
    color: #333;
    font-size: 14px;
    line-height: 1.75;
    text-align: justify;
}

.bold {
    font-weight: 700;
}

/* Skill */
.skill {
    margin-bottom: 17px;
}

.skill-name {
    font-size: 13px;
    font-weight: 800;
    color: #17365d;
    text-transform: uppercase;
    margin-bottom: 4px;
}

.skill-description {
    font-size: 13px;
    color: #444;
    line-height: 1.6;
}

/* Sở thích */
.hobby {
    display: flex;
    align-items: center;
    gap: 9px;
    margin: 9px 0;
    font-size: 13px;
    color: #444;
}

.hobby-dot {
    width: 7px;
    height: 7px;
    background: #17365d;
    border-radius: 50%;
    display: inline-block;
}

/* Education */
.timeline-item {
    margin-bottom: 23px;
    position: relative;
}

.date {
    color: #1f4e79;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 5px;
}

.organization {
    color: #222;
    font-size: 15px;
    font-weight: 800;
    text-transform: uppercase;
    margin-bottom: 5px;
}

.position {
    color: #555;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 7px;
}

.detail {
    color: #444;
    font-size: 13.5px;
    line-height: 1.7;
}

.detail ul {
    margin-top: 5px;
    padding-left: 20px;
}

.detail li {
    margin-bottom: 5px;
}

/* Certificate cards */
.certificate {
    background: white;
    border-left: 4px solid #1f4e79;
    padding: 12px 14px;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.certificate-year {
    color: #1f4e79;
    font-size: 12px;
    font-weight: 800;
}

.certificate-name {
    color: #333;
    font-size: 13px;
    font-weight: 700;
    margin-top: 3px;
}

/* Footer */
.cv-footer {
    text-align: center;
    padding: 16px;
    background: #17365d;
    color: white;
    font-size: 12px;
}

/* Responsive */
@media (max-width: 800px) {

    .cv-container {
        margin: 10px;
    }

    .cv-header {
        padding: 30px 25px;
    }

    .cv-name {
        font-size: 30px;
    }

    .contact-grid {
        grid-template-columns: 1fr;
    }

    .cv-body {
        grid-template-columns: 1fr;
    }

    .left-column {
        border-right: none;
        border-bottom: 1px solid #e4e7eb;
    }

    .right-column {
        padding: 30px 25px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="cv-container">

    <div class="cv-header">

        <div class="cv-name">
            ĐẶNG PHÚ HƯNG
        </div>

        <div class="cv-position">
            SINH VIÊN NĂM 3 NGÀNH TÀI CHÍNH NGÂN HÀNG
        </div>

        <div class="contact-grid">

            <div class="contact-item">
                <span class="contact-label">Ngày sinh:</span>
                05/07/2005
            </div>

            <div class="contact-item">
                <span class="contact-label">Giới tính:</span>
                Nam
            </div>

            <div class="contact-item">
                <span class="contact-label">Số điện thoại:</span>
                0909116235
            </div>

            <div class="contact-item">
                <span class="contact-label">Email:</span>
                phuhung5705@gmail.com
            </div>

            <div class="contact-item">
                <span class="contact-label">Website:</span>
                Facebook Profile
            </div>

            <div class="contact-item">
                <span class="contact-label">Địa chỉ:</span>
                80/21 Tô Vĩnh Diện, Khu phố Tân Hòa,
                Phường Đông Hòa, Thành phố Hồ Chí Minh
            </div>

        </div>

    </div>
""", unsafe_allow_html=True)


# =========================================================
# BODY - CHIA 2 CỘT
# =========================================================

st.markdown("""
<div class="cv-body">

    <!-- ================= CỘT TRÁI ================= -->

    <div class="left-column">

        <!-- HỌC VẤN -->

        <div class="section">

            <div class="section-title">
                Học vấn
            </div>

            <div class="timeline-item">

                <div class="date">
                    19/2023 - nay
                </div>

                <div class="organization">
                    Trường Đại học Nguyễn Tất Thành
                </div>

                <div class="position">
                    Chuyên ngành Tài chính ngân hàng
                </div>

                <div class="detail">

                    <b>• Xếp loại:</b> Khá
                    <br>

                    <b>• Chứng chỉ:</b>
                    Kỹ năng Hành chính văn phòng,
                    Kỹ năng làm chủ công việc

                </div>

            </div>

        </div>


        <!-- CHỨNG CHỈ -->

        <div class="section">

            <div class="section-title">
                Chứng chỉ
            </div>

            <div class="certificate">

                <div class="certificate-year">
                    2025
                </div>

                <div class="certificate-name">
                    KỸ NĂNG HÀNH CHÍNH VĂN PHÒNG
                </div>

            </div>

            <div class="certificate">

                <div class="certificate-year">
                    2025
                </div>

                <div class="certificate-name">
                    KỸ NĂNG LÀM CHỦ CÔNG VIỆC
                </div>

            </div>

        </div>


        <!-- KỸ NĂNG -->

        <div class="section">

            <div class="section-title">
                Kỹ năng
            </div>


            <div class="skill">

                <div class="skill-name">
                    Soạn thảo văn bản
                </div>

                <div class="skill-description">
                    Kỹ năng soạn thảo văn bản hành chính và học thuật.
                    Thành thạo Microsoft Word, trình bày văn bản chuyên nghiệp.
                    Kỹ năng viết và chỉnh sửa báo cáo.
                </div>

            </div>


            <div class="skill">

                <div class="skill-name">
                    Kỹ năng bàn phím
                </div>

                <div class="skill-description">
                    Kỹ năng bàn phím tốt, gõ nhanh và chính xác,
                    sử dụng thành thạo phím tắt trong Word và Excel.
                </div>

            </div>


            <div class="skill">

                <div class="skill-name">
                    Giải quyết vấn đề
                </div>

                <div class="skill-description">
                    Phân tích tình huống, xác định nguyên nhân,
                    đề xuất và lựa chọn giải pháp phù hợp.
                </div>

            </div>


            <div class="skill">

                <div class="skill-name">
                    Quản lý thời gian
                </div>

                <div class="skill-description">
                    Sắp xếp công việc theo mức độ ưu tiên,
                    đảm bảo hoàn thành đúng hạn, cân bằng học tập và công việc.
                </div>

            </div>

        </div>


        <!-- SỞ THÍCH -->

        <div class="section">

            <div class="section-title">
                Sở thích
            </div>

            <div class="hobby">
                <span class="hobby-dot"></span>
                Đọc sách
            </div>

            <div class="hobby">
                <span class="hobby-dot"></span>
                Nghe podcast học tập
            </div>

            <div class="hobby">
                <span class="hobby-dot"></span>
                Tham gia hoạt động học thuật
            </div>

            <div class="hobby">
                <span class="hobby-dot"></span>
                Tự học kỹ năng mềm
            </div>

        </div>

    </div>


    <!-- ================= CỘT PHẢI ================= -->

    <div class="right-column">

        <!-- MỤC TIÊU -->

        <div class="section">

            <div class="section-title">
                Mục tiêu nghề nghiệp
            </div>

            <div class="text">

                Áp dụng kiến thức chuyên ngành
                <b>Tài chính – Ngân hàng</b> cùng kỹ năng
                <b>Word, Excel và phân tích dữ liệu</b>
                để hỗ trợ hiệu quả các nghiệp vụ ngân hàng.

                Không ngừng học hỏi quy trình nghiệp vụ,
                nâng cao kỹ năng chuyên môn và hướng tới trở thành
                nhân sự ngân hàng chuyên nghiệp,
                có giá trị lâu dài cho tổ chức.

            </div>

        </div>


        <!-- HOẠT ĐỘNG -->

        <div class="section">

            <div class="section-title">
                Hoạt động
            </div>


            <!-- Hoạt động 2024 -->

            <div class="timeline-item">

                <div class="date">
                    11/05/2024 - 23/12/2024
                </div>

                <div class="organization">
                    Trường Đại học Nguyễn Tất Thành
                </div>

                <div class="position">
                    SINH VIÊN THAM GIA
                </div>

                <div class="detail">

                    <ul>

                        <li>
                            Tham gia UNITOUR nhà lãnh đạo tương lai
                            và giới thiệu cuộc thi ASEAN - CHINA - INDIA 2024.
                        </li>

                        <li>
                            Tham gia Ngày hội tuyển dụng tháng 5 năm 2024.
                        </li>

                        <li>
                            Tham gia Workshop Đầu tư chứng khoán
                            "Bản lĩnh đầu tư & tự tin chiến thắng".
                        </li>

                        <li>
                            Tham gia Chương trình Tìm hiểu tài nguyên
                            giáo dục mở cho Tân SV khóa 2024.
                        </li>

                    </ul>

                </div>

            </div>


            <!-- Hoạt động 2025 -->

            <div class="timeline-item">

                <div class="date">
                    09/08/2025 - 05/10/2025
                </div>

                <div class="organization">
                    Trường Đại học Nguyễn Tất Thành
                </div>

                <div class="position">
                    SINH VIÊN THAM GIA
                </div>

                <div class="detail">

                    <ul>

                        <li>
                            Tham gia Hội thảo khoa học Quốc tế
                            Toán học và Ứng dụng năm 2025.
                        </li>

                        <li>
                            Tham gia Hoạt động phục vụ cộng đồng cấp Khoa 2025
                            - Hành trình tuổi trẻ vì cộng đồng 2025 -
                            Trung thu nghĩa tình 2025.
                        </li>

                    </ul>

                </div>

            </div>

        </div>

    </div>

</div>


<!-- FOOTER -->

<div class="cv-footer">
    CV - ĐẶNG PHÚ HƯNG
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# NÚT TẢI / IN CV
# =========================================================

st.markdown("""
<div style="
    max-width:1100px;
    margin:20px auto;
    text-align:center;
">

<p style="
    color:#666;
    font-size:13px;
">
Bạn có thể sử dụng chức năng Print của trình duyệt
để lưu CV thành PDF.
</p>

</div>
""", unsafe_allow_html=True)
